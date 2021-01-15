def on_a_pressed():
    if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite.vy = -200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite, location):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_closed_south,
    on_overlap_tile)

def on_overlap_tile2(sprite, location):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player, myTiles.tile1, on_overlap_tile2)

mySprite: Sprite = None
scene.set_background_color(9)
tiles.set_tilemap(tiles.create_tilemap(hex("""
            3200080000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000050000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000040202020202020202020101020202020201010101020202020202020202010102020202020101020202020201010202020202
        """),
        img("""
            ..................................................
                ..................................................
                ..................................................
                ..................................................
                ..................................................
                ..................................................
                ..................................................
                222222222..22222....222222222..22222..22222..22222
        """),
        [myTiles.transparency16,
            myTiles.tile1,
            sprites.vehicle.road_horizontal,
            sprites.dungeon.door_closed_north,
            sprites.dungeon.door_closed_south,
            sprites.dungeon.door_open_south],
        TileScale.SIXTEEN))
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . 6 6 6 6 6 6 6 6 . . . . 
            . . . 6 9 6 6 6 6 6 6 c 6 . . . 
            . . 6 c 9 6 6 6 6 6 6 c c 6 . . 
            . 6 c c 9 9 9 9 9 9 6 c c 9 6 d 
            . 6 c 6 8 8 8 8 8 8 8 b c 9 6 6 
            . 6 6 8 b b 8 b b b 8 8 b 9 6 6 
            . 6 8 b b b 8 b b b b 8 6 6 6 6 
            . 8 8 6 6 6 8 6 6 6 6 6 8 6 6 6 
            . 8 8 8 8 8 8 f 8 8 8 f 8 6 d d 
            . 8 8 8 8 8 8 f 8 8 f 8 8 8 6 d 
            . 8 8 8 8 8 8 f f f 8 8 8 8 8 8 
            . 8 f f f f 8 8 8 8 f f f 8 8 8 
            . . f f f f f 8 8 f f f f f 8 . 
            . . . f f f . . . . f f f f . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
mySprite.ay = 400
mySprite.ax = 100
scene.camera_follow_sprite(mySprite)