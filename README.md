# Beary

![Serial Experiments Lain: The eponymous character sits in a dark room wearing her signature teddy bear pajamas, hood up.  In the background, a small piece of electronics sits on her desk, flickering ominously.](./graphics/lain_bear.gif)

Beary is a Pythonic wrapper for [bearlibterminal](http://foo.wyrd.name/en:bearlibterminal) by [cfyzium](http://foo.wyrd.name/).  It's built on top of the provided Python library, which is more or less a direct mapping to the C bindings.

The purpose of this API is allow you to easily create pseudoterminal applications which work cross-platform and are much more capable than a stanard terminal.

Fancy bearlibterminal features include:

* Full RGB (plus alpha) color channels
* Arbitrary positioning
* Graphics support

## Installation

> pip install beary

Or...

> git clone git@github.com:Yuffster/beary.git
>
> cd beary
>
> python setup.py install

## Examples

I'm currently porting all the bearlib native examples to the Beary API.  You can view the full source code in the [examples](./examples/) directory.

### Basic Output

View the [full source](./examples/basic_output.py)

![A terminal screen showing a wide variety of colors, unicode characters, and tile composition.](./graphics/examples/basic_output.png)