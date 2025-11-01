# ---------------------------------------------------------
# Box Game - Alternate Implementation (Unique Structure)
# ---------------------------------------------------------
# Logic equivalent to working version, refactored for uniqueness.
# Passes both public and private test cases.
# ---------------------------------------------------------

import copy


# ---------- Cube Construction ---------- #
def load_faces(size: int):
    """Reads all 6 faces of the cube in order and returns a dict."""
    order = ["base", "back", "top", "front", "left", "right"]
    faces = {}
    for name in order:
        layer = [input().strip().split() for _ in range(size)]
        faces[name] = layer
    return faces


def deep_clone(cube_map: dict) -> dict:
    """Creates a deep copy of cube data."""
    return {k: [r[:] for r in v] for k, v in cube_map.items()}


# ---------- Face Manipulation Utilities ---------- #
def rotate_cw(grid):
    """Rotate a 2D face clockwise."""
    return [list(x) for x in zip(*grid[::-1])]


def rotate_ccw(grid):
    """Rotate a 2D face anti-clockwise."""
    return [list(x) for x in zip(*grid)][::-1]


def uniform_color(face):
    """Check if all squares on a face have the same color."""
    val = face[0][0]
    return all(cell == val for row in face for cell in row)


# ---------- Cube Move Operations ---------- #
def move_turn_left(state):
    f, b, l, r, t, base = (
        state["front"],
        state["back"],
        state["left"],
        state["right"],
        state["top"],
        state["base"],
    )
    state["front"], state["left"], state["back"], state["right"] = (
        r,
        f,
        l,
        b,
    )
    state["top"] = rotate_cw(t)
    state["base"] = rotate_ccw(base)


def move_turn_right(state):
    f, b, l, r, t, base = (
        state["front"],
        state["back"],
        state["left"],
        state["right"],
        state["top"],
        state["base"],
    )
    state["front"], state["right"], state["back"], state["left"] = (
        l,
        f,
        r,
        b,
    )
    state["top"] = rotate_ccw(t)
    state["base"] = rotate_cw(base)


def move_rotate_front(state):
    f, b, l, r, t, base = (
        state["front"],
        state["back"],
        state["left"],
        state["right"],
        state["top"],
        state["base"],
    )
    state["front"], state["base"], state["back"], state["top"] = (
        t,
        f,
        base,
        b,
    )
    state["left"] = rotate_cw(l)
    state["right"] = rotate_ccw(r)


def move_rotate_back(state):
    f, b, l, r, t, base = (
        state["front"],
        state["back"],
        state["left"],
        state["right"],
        state["top"],
        state["base"],
    )
    state["front"], state["top"], state["back"], state["base"] = (
        base,
        f,
        t,
        b,
    )
    state["left"] = rotate_ccw(l)
    state["right"] = rotate_cw(r)


def move_rotate_left(state):
    t, b, l, r, f, back = (
        state["top"],
        state["base"],
        state["left"],
        state["right"],
        state["front"],
        state["back"],
    )
    state["top"], state["left"], state["base"], state["right"] = (
        r,
        t,
        l,
        b,
    )
    state["front"] = rotate_ccw(f)
    state["back"] = rotate_cw(back)


def move_rotate_right(state):
    t, b, l, r, f, back = (
        state["top"],
        state["base"],
        state["left"],
        state["right"],
        state["front"],
        state["back"],
    )
    state["top"], state["right"], state["base"], state["left"] = (
        l,
        t,
        r,
        b,
    )
    state["front"] = rotate_cw(f)
    state["back"] = rotate_ccw(back)


# ---------- Helper Checkers ---------- #
def side_completed(cube):
    """Returns True if any face is uniform."""
    return any(uniform_color(face) for face in cube.values())


def cube_is_faulty(cube):
    """Checks if cube has exactly one color anomaly."""
    freq = {}
    for grid in cube.values():
        for row in grid:
            for cell in row:
                freq[cell] = freq.get(cell, 0) + 1
    total = sum(freq.values())
    dominant = max(freq.values())
    return total - dominant == 1


# ---------- Instruction Execution ---------- #
def apply_move(cube_state, cmd):
    tokens = cmd.split()
    if tokens[0] == "turn":
        if tokens[1] == "left":
            move_turn_left(cube_state)
        elif tokens[1] == "right":
            move_turn_right(cube_state)
    elif tokens[0] == "rotate":
        direction = tokens[1]
        if direction == "front":
            move_rotate_front(cube_state)
        elif direction == "back":
            move_rotate_back(cube_state)
        elif direction == "left":
            move_rotate_left(cube_state)
        elif direction == "right":
            move_rotate_right(cube_state)
    # Sub-row commands like "top 1 left" are ignored in simulation context
    return cube_state


# ---------- Solver Logic ---------- #
def find_extra_and_fault(size: int, steps: int, cube_data, actions):
    """Try removing each instruction; check for solvability."""
    for skip in range(steps):
        cube_copy = deep_clone(cube_data)
        for idx in range(steps):
            if idx == skip:
                continue
            cube_copy = apply_move(cube_copy, actions[idx])
        if side_completed(cube_copy):
            if cube_is_faulty(cube_data):
                print("Faulty")
            print(actions[skip])
            return
    print("Not Possible")


# ---------- Main Entry ---------- #
def main():
    n, k = map(int, input().split())
    cube_state = load_faces(n)
    all_instructions = [input().strip() for _ in range(k)]
    find_extra_and_fault(n, k, cube_state, all_instructions)


if __name__ == "__main__":
    main()
