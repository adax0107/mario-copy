def on_a_pressed():
    if ali.vy == 0:
        ali.vy = -150
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

ali: Sprite = None
tiles.set_tilemap(tilemap("""
    level
"""))
ali = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . f f f f f f . . . . . 
            . . . f f e e e e f 2 f . . . . 
            . . f f e e e e f 2 2 2 f . . . 
            . . f e e e f f e e e e f . . . 
            . . f f f f e e 2 2 2 2 e f . . 
            . . f e 2 2 2 f f f f e 2 f . . 
            . f f f f f f f e e e f f f . . 
            . f f e 4 4 e b f 4 4 e e f . . 
            . f e e 4 d 4 1 f d d e f f . . 
            . . f e e e 4 d d d d f d d f . 
            . . . . f e e 4 e e e f b b f . 
            . . . . f 2 2 2 4 d d e b b f . 
            . . . f f 4 4 4 e d d e b f . . 
            . . . f f f f f f e e f f . . . 
            . . . . f f . . . f f f . . . .
    """),
    SpriteKind.player)
tiles.place_on_random_tile(ali, sprites.dungeon.collectible_insignia)
controller.move_sprite(ali, 100, 0)
ali.ay = 300
scene.camera_follow_sprite(ali)

def on_on_update():
    if ali.y > 232:
        game.over(False, effects.slash)
game.on_update(on_on_update)
