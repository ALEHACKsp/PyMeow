# PyMeow
#### Python Library for external Game Hacking created with [Nim](https://nim-lang.org)

##### <ins>Memory API</ins>
```
process_by_name(name: string) -> Process
wait_for_process(name: string) -> Process
enumerate_processes() -> Process (iterator)
close(Process) -> bool

read_string(Process, address: int) -> string
read_int(Process, address: int) -> int
read_ints(Process, address: int, size: int) -> int array
read_uint(Process, address: int) -> int
read_uints(Process, address: int, size: int) -> int array
read_int16(Process, address: int) -> int16
read_ints16(Process, address: int) -> int16 array
read_int64(Process, address: int) -> int64
read_ints64(Process, address: int, size: int) -> int64 array
read_float(Process, address: int) -> float
read_floats(Process, address: int, size: int) -> float array
read_float64(Process, address: int) -> float64
read_floats64(Process, address: int, size: int) -> float64 array
read_byte(Process, address: int) -> byte
read_bytes(Process, address: int, size: int) -> byte array
read_vec2(Process, address: int) -> vec2
read_vec3(Process, address: int) -> vec3
read_bool(Process, address: int) -> bool

write_int(Process, address: int, data: int)
write_ints(Process, address: int, data: int array)
write_int16(Process, address: int, data: int)
write_ints16(Process, address: int, data: int array)
write_int64(Process, address: int, data: int)
write_ints64(Process, address: int, data: int array)
write_float(Process, address: int, data: float)
write_floats(Process, address: int, data: float array)
write_byte(Process, address: int, data: byte)
write_bytes(Process, address: int, data: byte array)
write_vec2(Process, address: int, data: Vec2)
write_vec3(Process, address: int, data: Vec3)
write_bool(Process, address: int, data: bool)

dma_addr(Process, baseAddr: int, offsets: array) -> int
aob_scan(Process, pattern: string, module: Process["modules"]["moduleName"] -> int
nop_code(Process, address: int, length: int)
patch_bytes(Process, address: int, data: byte array)
inject_dll(Process, dllPath: string)
page_protection(Process, address: int, newProtection: int = 0x40) -> int (old protection)
```
##### <ins>Overlay API</ins>
```
overlay_init(target: string = "Fullscreen", borderOffset: int = 25) -> Overlay
overlay_close(Overlay)
overlay_deinit()
overlay_loop(Overlay) -> bool
overlay_set_pos(Overlay, x, y: int)
```
##### <ins>Drawing API</ins>
```
font_init(height: int, fontName: string) -> Font
font_deinit(Font)
font_print(Font, x, y: float, text: string, color: rgb array)

box(x, y, width, height, lineWidth: float, color: rgb array)
alpha_box(x, y, width, height: float, color, outlineColor: rgb array, alpha: float)
line(x1, y1, x2, y2, lineWidth: float, color: rgb array)
dashed_line(x1, y1, x2, y2, lineWidth: float, color: rgb array, factor: int = 2, pattern: string = "11111110000", alpha: float = 0.5)
circle(x, y, radius: float, color: rgb array, filled: bool = true)
rad_circle(x, y, radius: float, value: int, color: rgb array)
triangle(x1, y1, x2, y2, x3, y3: float, color: rgb array, alpha: float)
value_bar(x1, y1, x2, y2, width, maxValue, value: float, vertical: bool = true)
```
##### <ins>Vector API</ins>
```
vec2(x, y: float = 0) -> Vec2
vec2_add(a, b: Vec2) -> Vec2
vec2_del(a, b: Vec2) -> Vec2
vec2_mult(a, b: Vec2) -> Vec2
vec2_div(a, b: Vec2) -> Vec2
vec2_mag(a, b: Vec2) -> float
vec2_magSq(a, b: Vec2) -> float
vec2_distance(a, b: Vec2) -> float
vec2_closest(a: Vec2, b: Vec2 array) -> Vec2

vec3(x, y, z: float = 0) -> Vec3
vec3_add(a, b: Vec3) -> Vec3
vec3_sub(a, b: Vec3) -> Vec3
vec3_mult(a, b: Vec3) -> Vec3
vec3_div(a, b: Vec3) -> Vec3
vec3_mag(a, b: Vec3) -> float
vec3_magSq(a, b: Vec3) -> float
vec3_distance(a, b: Vec3) -> float
vec3_closest(a: Vec2, b: Vec3 array) -> Vec3
```
##### <ins>Misc</ins>
```
key_pressed(vKey: int) -> bool
rgb(color: string) -> float array
wts_ogl(Overlay, matrix: float array (16), pos: Vec3) -> Vec2
wts_dx(Overlay, matrix: float array (16), pos: Vec3) -> Vec2
set_foreground(title: string)
mouse_click()
mouse_move(overlay: Overlay, x, y: float)
```

## [CSGo ESP](https://github.com/Sann0/PyMeow/blob/master/examples/csgo_esp.py):
![Alt text](https://github.com/Sann0/PyMeow/blob/master/examples/screenshots/csgo_py.png=250x)

## [Assault Cube ESP](https://github.com/Sann0/PyMeow/blob/master/examples/ac_esp.py)
![Alt text](https://github.com/Sann0/PyMeow/blob/master/examples/screenshots/ac2_py.png)

## [Assault Cube Mem Hacks](https://github.com/Sann0/PyMeow/blob/master/examples/ac_hacks.py):
![Alt text](https://github.com/Sann0/PyMeow/blob/master/examples/screenshots/ac_py.png)

## [SWBF2 ESP](https://github.com/Sann0/PyMeow/blob/master/examples/swbf2_esp.py)
![Alt text](https://github.com/Sann0/PyMeow/blob/master/examples/screenshots/swbf_py.png)

## [Cube2: Sauberbraten ESP + Aimbot](https://github.com/Sann0/PyMeow/blob/master/examples/sauerbraten_espaim.py)
[<img src="https://img.youtube.com/vi/7F_16FQURGc/maxresdefault.jpg" width="50%">](https://youtu.be/7F_16FQURGc)

## [Healthbar](https://github.com/Sann0/PyMeow/blob/master/examples/healthbar.py)
![Alt text](https://github.com/Sann0/PyMeow/blob/master/examples/screenshots/healthbar.gif)

###### credits to: [nimpy](https://github.com/yglukhov/nimpy), [winim](https://github.com/khchen/winim), [nimgl](https://github.com/nimgl/nimgl), [GuidedHacking](https://guidedhacking.com)