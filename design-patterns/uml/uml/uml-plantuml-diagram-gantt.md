```plantuml
@startgantt

Project starts 2000-01-01
2000-01-26 to 2000-01-28 are colored in salmon
saturday are closed
sunday are closed

-- Version v1.0 --

[Prototype] starts 2000-01-05
[Prototype] lasts 18 days
[Prototype] is colored in Lavender

[Testing] starts 2000-01-31
[Testing] lasts 10 days
[Testing] is colored in LightBlue

-- Version v2.0 --

[MVP] starts 2000-01-15
[MVP] lasts 10 days
then [Test] lasts 5 days
```
