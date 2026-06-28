\# LuxeForge Studio



\# RELEASE



\## Current Release



\*\*Version\*\*



0.2.0-alpha



\*\*Release Name\*\*



Geometry Foundation



\*\*Status\*\*



Development



\---



\# Summary



This release establishes the technical foundation of LuxeForge Studio.



The project now contains the first version of the procedural geometry engine and the Blender integration required for future development.



This release focuses on architecture, stability and maintainability rather than visual features.



\---



\# Features



\## Blender Add-on



\* Blender 5.x support

\* Sidebar panel

\* Generate button

\* Automatic object creation



\---



\## Geometry Engine



\* Path

\* Point

\* Mesh Builder

\* Extruder (foundation)



\---



\## Core



\* Parameter model

\* Bag service

\* Body engine

\* Logging

\* Version management



\---



\# Repository



Current structure



```text

docs/

src/

tests/

tools/

release/

```



The project is now split into:



\* Core Engine

\* Blender Integration

\* Documentation

\* Build Tools



\---



\# Current Milestone



\## Geometry Engine



Progress



\* ✅ Repository restructure

\* ✅ Build system

\* ✅ Documentation

\* ✅ Path class

\* ✅ Mesh Builder

\* 🚧 Extruder

\* ⬜ Curves

\* ⬜ Fillets

\* ⬜ Rounded Body



\---



\# Known Limitations



Current body generation is still based on a simple profile.



Rounded procedural geometry has not yet been implemented.



The Geometry Engine is still under active development.



\---



\# Development Rules



Every release must satisfy:



\* Builds successfully

\* Loads in Blender

\* No Python exceptions

\* Existing functionality remains operational



No release should intentionally break previously working features.



\---



\# Next Release



Version



0.3.0-alpha



Planned features



\* CAD Path Engine

\* Procedural Curves

\* Rounded Corners

\* First Luxury Body

\* Improved Geometry Pipeline



\---



\# Long-Term Vision



LuxeForge Studio is not intended to be a collection of Blender scripts.



Its goal is to become a modular CAD engine for designing luxury accessories using procedural geometry.



Blender is the first supported platform.



Future platforms may include standalone desktop applications, web interfaces and additional CAD integrations.



