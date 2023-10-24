# Proj Forge

A site like <epsg.io> with rich information about data in the Proj database,
except it's updated automatically.

> [!IMPORTANT]
>
> This is a prototype. Manual action is still required to upgrade the data
> dependency and rebuild the site.

## Rationale

The _EPSG database_ is distributed by EPSG.org, but their website is not as
accessible as I'd like. It only offers WKT and GMT export formats.

[EPSG.io](https://github.com/maptiler/epsg.io) is an open-source project owned
by MapTiler that makes the EPSG database more accessible and interoperable, but
hasn't been updated alongside the official EPSG database for years. EPSG.io is
often linked by documentation (for example, on NSIDC.org) over the official
website because it is more accessible and interoperable. EPSG.io is sometimes
perceived as an official website because of the added value it provides, and the
end result is that an out-of-date resource is treated as a source of truth.

The current goal of this project is to provide added value people rely on (if
it's not there, you can add it with a PR!) while keeping the actual data
up-to-date and correct using automations.

### And more...

The long-term tentative goal of this project is to find a way to make the
management of the EPSG database more open and community-led. Projects like
EPSG.io and this one are arising out of real community needs, and moving
currently-private e-mail discussions about the database into the public sphere
seems, to me, to be a good first step.

I think it's a common misconception to construe "community" as "any random
person on the street" and fear that engagement will reduce quality. The
community of people interested in this data and working with this data is rich
and diverse, spanning research and industry, and contains a wealth of expertise.

The name "Proj Forge" arose out of this long-term vision. Currently we don't
"forge" anything, we just make data already in the _Proj_ database accessible on
the web.

## Built on

The _Proj_ project is based on the EPSG database. It enriches the data and
redistributes it as a SQLite3 database. Open source language bindings are built
on top of this, and our project uses _pyproj_ to work with the data within
Python.

_Jinja_ is used to render HTML pages from templates for each CRS.

GitHub Actions and GitHub Pages are used to build and host the ~13,000 output
HTML pages.

## TODO

- :star: Automate updating the _pyproj_ dependency and re-rendering the website.
- "Projections" doesn't accurately describe the data we can make more
  accessible. Neither does CRS; I expect to be able to display projected CRSes,
  geographic CRSes, datums, ellipsoids, spheroids, etc. What do we call that
  class of things?\_
- Continue cleanup/adaption of stuff initialized from the Scientific Python
  project template. Not everything was as I'd like it, and I think there's a lot
  we don't need that we haven't cleaned up yet. _Contribute fixes back to the
  Scientific Python project!_
- Enable accessing old versions of the dataset. Right now the data is ~100MB,
  and I think GitHub Pages' limit is 1GB, so we'd start to incur costs if we
  store too much history.

## Acknowledgements

Prototype developed in a group programming session with
[Arie Knoester](https://github.com/arieknoester),
[Robin Fisher](https://github.com/itsarobin).

Inspired by discussions with [Trey Stafford](https://github.com/trey-stafford/).

Inspired by discussions with and
[prototype](https://github.com/andypbarrett/epsg-site-demo) by
[Andy Barrett](https://github.com/andypbarrett).
