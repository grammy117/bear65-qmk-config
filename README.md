# bear65-qmk-config

QMK keymap for the **Bear 65 rev1** (`jacky_studio/bear_65/rev1`, ATmega32U4, Atmel DFU), ported from my [Temper ZMK config](https://github.com/grammy117/temper-zmk-config).

- `build_keymap.py` is the source of truth; it generates `bear65_gram.json`.
- `bear65_gram.json` can be imported at [config.qmk.fm](https://config.qmk.fm) or built with `qmk compile bear65_gram.json`.
- Every push builds a `.hex` with GitHub Actions; download it from the run's **Artifacts** (`bear65-firmware`).

## Flashing

1. Enter the bootloader: hold **Esc** while plugging in (bootmagic), or press **top-right + Esc** (`QK_BOOT`) on the new firmware.
2. Open the `.hex` in [QMK Toolbox](https://qmk.fm/toolbox) and click **Flash**.
3. First time on Windows: QMK Toolbox → Tools → Install Drivers (the DFU device needs WinUSB).

## Layers

Hold-tap timing approximates the ZMK `balanced` behavior: 280 ms tapping term, permissive hold, 120 ms flow tap.

### 0 · Base

```
Mute  `   1  2  3  4  5  6        7  8  9  0  -  =  Bksp Del     [EXTRA]
Vol+  Tab   Q  W  E  R  T       Y  U  I  O  P  [  ]  \
Vol-  Esc    A  S  D  F  G     H  J  K  L  ;  '  Enter
      Shift    Z  X  C  V  B   B  N  M  ,  .  /  Shift  Up
      Ctrl  [NUM]  [ Bksp ] [Shift]   [  Space  ] [SYM]    Left Down Right
```

Home-row mods: A=GUI S=Ctrl D=Alt F=Shift / J=Shift K=Alt L=Ctrl ;=GUI (hold).

### 1 · SYM (hold right thumb key)

```
  `  @  #  $  %       ·  (  )  %  ^
  !  \  '  "  ·       _  {  }  &  *
  ·  ·  ~  |  ·    -  -  [  ]  .  +
  thumb: [NUM] key → EXTRA
```

### 2 · NUM (hold left thumb key)

```
  End   Del   Esc   Tab   Home      +  7  8  9  *
  Left  Down  Up    Right Tab       =  4  5  6  0     (home-row mods)
  PrtSc PrtSc PgDn  PgUp  ·      -  -  1  2  3  /
  thumb: [SYM] key → EXTRA
```

### 3 · EXTRA (hold top-right key, or NUM + SYM)

```
EE_CLR QK_BOOT F1 .. F12 (number row)               Reboot
RGB tog  RGB next  F1  F2  F3  F4  F5     Hue+ Sat+ Val+ Spd+ BL+  BL tog
RGB prev   ·       F6  F7  F8  F9  F10    Hue- Sat- Val- Spd- BL-  BL breathe
           F11 F12 Prev Play Next      Play Bri- Bri+                Vol+
                                                           Prev Vol- Next
```

`QK_BOOT` sits on the Esc key, opposite the top-right layer key, so it can't be hit by accident.
