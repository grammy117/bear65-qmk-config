"""Generates bear65_gram.json (QMK Configurator / qmk compile keymap) for jacky_studio/bear_65/rev1, LAYOUT_all.

Ported from gram-117/gergobt-zmk-config (Temper 3x5+3).
Layers: 0 BASE, 1 KEY (symbols), 2 NUM (numpad/nav), 3 EXTRA (F-keys, RGB, media, QK_BOOT).
"""
import json

_ = "KC_TRNS"
X = "KC_NO"

# Home-row mods (Temper: GUI / CTRL / ALT / SHIFT on A S D F, mirrored on J K L ;)
def hrm_l(a, s, d, f):
    return [f"LGUI_T({a})", f"LCTL_T({s})", f"LALT_T({d})", f"LSFT_T({f})"]
def hrm_r(j, k, l, sc):
    return [f"RSFT_T({j})", f"RALT_T({k})", f"RCTL_T({l})", f"RGUI_T({sc})"]

def layer(r0, r1, r2, r3, r4):
    rows = [r0, r1, r2, r3, r4]
    want = [17, 15, 14, 14, 9]
    for i, (r, n) in enumerate(zip(rows, want)):
        assert len(r) == n, f"row {i}: {len(r)} != {n}"
    return [k for r in rows for k in r]

# Positions in LAYOUT_all order:
# r0: [Lcol] [`/Esc] 1 2 3 4 5 6 | 7 8 9 0 - = [Bksp] [Bksp-split] | [TopRight]
# r1: [Lcol] Tab Q W E R T | Y U I O P [ ] \
# r2: [Lcol] Caps A S D F G | H J K L ; ' Enter
# r3: LShift Z X C V B | B N M , . / RShift Up
# r4: LCtrl LAlt [LSpace 2.25] [1u mid] | [RSpace 2.75] [1.5u] Left Down Right

BASE = layer(
    ["KC_MUTE", "KC_GRV", "KC_1", "KC_2", "KC_3", "KC_4", "KC_5", "KC_6",
     "KC_7", "KC_8", "KC_9", "KC_0", "KC_MINS", "KC_EQL", "KC_BSPC", "KC_DEL", "MO(3)"],
    ["KC_VOLU", "KC_TAB", "KC_Q", "KC_W", "KC_E", "KC_R", "KC_T",
     "KC_Y", "KC_U", "KC_I", "KC_O", "KC_P", "KC_LBRC", "KC_RBRC", "KC_BSLS"],
    ["KC_VOLD", "KC_ESC", *hrm_l("KC_A", "KC_S", "KC_D", "KC_F"), "KC_G",
     "KC_H", *hrm_r("KC_J", "KC_K", "KC_L", "KC_SCLN"), "KC_QUOT", "KC_ENT"],
    ["KC_LSFT", "KC_Z", "KC_X", "KC_C", "KC_V", "KC_B",
     "KC_B", "KC_N", "KC_M", "KC_COMM", "KC_DOT", "KC_SLSH", "KC_RSFT", "KC_UP"],
    ["KC_LCTL", "MO(2)", "KC_BSPC", "KC_LSFT",
     "KC_SPC", "MO(1)", "KC_LEFT", "KC_DOWN", "KC_RGHT"],
)

# KEY layer: Temper symbol layer on the alpha block. No mod-taps on shifted
# symbols (QMK mod-taps can't send shifted keycodes).
KEY = layer(
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, "KC_GRV", "KC_AT", "KC_HASH", "KC_DLR", "KC_PERC",
     _, "KC_LPRN", "KC_RPRN", "KC_PERC", "KC_CIRC", _, _, _],
    [_, _, "KC_EXLM", "KC_BSLS", "KC_QUOT", "KC_DQUO", _,
     "KC_UNDS", "KC_LCBR", "KC_RCBR", "KC_AMPR", "KC_ASTR", _, _],
    [_, _, _, "KC_TILD", "KC_PIPE", _,
     "KC_MINS", "KC_MINS", "KC_LBRC", "KC_RBRC", "KC_DOT", "KC_PLUS", _, _],
    [_, "MO(3)", _, _,
     _, _, _, _, _],
)

# NUM layer: nav on the left (with home-row mods, arrows are basic keycodes so
# mod-taps work), numpad on the right.
NUM = layer(
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, "KC_END", "KC_DEL", "KC_ESC", "KC_TAB", "KC_HOME",
     "KC_PLUS", "KC_7", "KC_8", "KC_9", "KC_ASTR", _, _, _],
    [_, _, *hrm_l("KC_LEFT", "KC_DOWN", "KC_UP", "KC_RGHT"), "KC_TAB",
     "KC_EQL", *hrm_r("KC_4", "KC_5", "KC_6", "KC_0"), _, _],
    [_, "KC_PSCR", "KC_PSCR", "KC_PGDN", "KC_PGUP", _,
     "KC_MINS", "KC_MINS", "KC_1", "KC_2", "KC_3", "KC_SLSH", _, _],
    [_, _, _, _,
     _, "MO(3)", _, _, _],
)

# EXTRA layer: reach by holding the top-right key, or NUM+KEY thumbs together.
# F-keys (Temper positions + number row), media, RGB underglow + backlight,
# and QK_BOOT on the Esc/` key (opposite hand from the top-right layer key,
# so it can't be hit by accident).
EXTRA = layer(
    ["EE_CLR", "QK_BOOT", "KC_F1", "KC_F2", "KC_F3", "KC_F4", "KC_F5", "KC_F6",
     "KC_F7", "KC_F8", "KC_F9", "KC_F10", "KC_F11", "KC_F12", _, "QK_RBT", _],
    ["UG_TOGG", "UG_NEXT", "KC_F1", "KC_F2", "KC_F3", "KC_F4", "KC_F5",
     "UG_HUEU", "UG_SATU", "UG_VALU", "UG_SPDU", "BL_UP", "BL_TOGG", _, _],
    ["UG_PREV", _, "KC_F6", "KC_F7", "KC_F8", "KC_F9", "KC_F10",
     "UG_HUED", "UG_SATD", "UG_VALD", "UG_SPDD", "BL_DOWN", "BL_BRTG", _],
    [_, "KC_F11", "KC_F12", "KC_MPRV", "KC_MPLY", "KC_MNXT",
     "KC_MPLY", "KC_BRID", "KC_BRIU", _, _, _, _, "KC_VOLU"],
    [_, _, _, _,
     _, _, "KC_MPRV", "KC_VOLD", "KC_MNXT"],
)

keymap = {
    "version": 1,
    "notes": "Bear65 port of gram-117 Temper ZMK config. L0 base, L1 symbols (right thumb), L2 num/nav (left thumb), L3 extra/RGB/QK_BOOT (top-right key or both thumbs).",
    "documentation": "Import at config.qmk.fm or build with: qmk compile bear65_gram.json",
    "keyboard": "jacky_studio/bear_65/rev1",
    "keymap": "gram_temper",
    "layout": "LAYOUT_all",
    "layers": [BASE, KEY, NUM, EXTRA],
    # Approximates the ZMK 'balanced' hold-tap: 280ms term, permissive hold,
    # require-prior-idle 120ms -> flow tap.
    "config": {
        "tapping": {
            "term": 280,
            "permissive_hold": True,
            "flow_tap_term": 120,
        }
    },
    "author": "gram-117",
}

with open("bear65_gram.json", "w") as f:
    json.dump(keymap, f, indent=2)
print("layers:", [len(l) for l in keymap["layers"]])
