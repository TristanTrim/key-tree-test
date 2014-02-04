key-tree-test
=============

Testing binary based key interface. Eventually it could run using a spiff type glove, but this test uses five keyboard keys.

Currently uses pygames and python2.

Plans
=====

I think I will extend and experiment with just text editing using pygame. Then once I have better ideas about it I'll rewrite it so that it has access to modkeys and the greater system. Finally I want to make a glove type thing with buttons on the finger tips to control/ type with.

How to type:
============

The keys are mapped to the binary sequence, so if you press "p" that would be a 1 or "a" key, then you would press "9" for 2 or "b" key, then you press "9" and "p".

I'm using the keys "space" "u" "8" "9" and "p" because on my keyboard the do not conflict with one another. I hope it is the same on yours, however my laptop doesn't work with it. I don't really know much about keyboard differences. It's likely to be hit and miss. If there are collisions then two keys will not work together and you will get a different letter for some key combonations.

It may be helpful to learn [finger binary](http://en.wikipedia.org/wiki/Finger_binary) before trying to use this keyboard. Right now it only uses little endian, and the finger binary article uses big endian, but it's pretty easy to learn the other once you know one.

All valid keypresses would be:

  ....p

  ...9.

  ...9p

  ..8..

  ..8.p

  ..89.

  ..89p

  .u...

  .u..p

  .u.9.

  .u.9p

  .u8..

  .u8.p

  .u89.

  .u89p

  S....

  S...p

  S..9.

  S..9p

  S.8..

  S.8.p

  S.89.

  S.89p

  Su...

  Su..p

  Su.9.

  Su.9p

  Su8..

  Su8.p

  Su89.

  Su89p


