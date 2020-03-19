#!/bin/sh

DEST_DIR=../../original_images/ch05

convert -crop 400x600+0+0 note-1.png $DEST_DIR/note-1-top.png
convert -crop 800x600+0+0 note-2.png $DEST_DIR/note-2-top.png
convert -crop 800x400+0+0 -gravity SouthWest note-2.png $DEST_DIR/note-2-bottom.png
