<h1>Expansion Panel</h1>

[![CI/CD Status][github-action-badge]][github-action-link] [![Codecov][codecov-badge]][codecov-project] [![MIT License][license-image]][license-url]  
[![NPM version][npm-version-image]][npm-package] [![Library size][file-size-badge]][raw-distribution-js]

Expansion panel & accordion components.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## Table of Contents

- [Installation](#installation)
  - [Packages that need to be installed](#packages-that-need-to-be-installed)
  - [Modules that need to be in NgModule](#modules-that-need-to-be-in-ngmodule)
  - [CSS imports](#css-imports)
  - [CSS resources](#css-resources)
- [Usage](#usage)
  - [Panel](#panel)
    - [Title and description](#title-and-description)
    - [Disable a panel](#disable-a-panel)
    - [Default a panel open](#default-a-panel-open)
    - [Lazy loaded content](#lazy-loaded-content)
    - [Transparent mode](#transparent-mode)
    - [Panel events](#panel-events)
    - [Custom trigger heights](#custom-trigger-heights)
    - [Manual control](#manual-control)
  - [Accordion](#accordion)
    - [Allow multiple panels to be open](#allow-multiple-panels-to-be-open)
    - [Accordion events](#accordion-events)
    - [Accordion as a stepper](#accordion-as-a-stepper)
    - [Hide toggle](#hide-toggle)
    - [Action row](#action-row)
    - [Open or close all panels](#open-or-close-all-panels)
- [Test Helpers](#test-helpers)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Installation

### Packages that need to be installed

- `@angular/cdk`
- `@angular/common`
- `@angular/core`
- `@angular/flex-layout`
- `@angular/forms`
- `@angular/platform-browser`
- `@terminus/design-tokens`
- `@terminus/fe-utilities`
- `@terminus/ui-utilities`
- `@terminus/ui-expansion-panel`
- `date-fns`

Use the `ng add` command to quickly install all the needed dependencies:

```bash
ng add @terminus/ui-expansion-panel
```

### Modules that need to be in NgModule

- `BrowserAnimationsModule,`
- `TsExpansionPanelModule,`

### CSS imports

In your top level stylesheet, add these imports:

```css
@import '~@terminus/design-tokens/css/library-design-tokens.css';
@import '~@terminus/ui-styles/terminus-ui.css';
```  

### CSS resources

Load the needed font families by adding this link to the `<head>` of your application:

```css
<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
```

## Usage

### Panel

The most basic usage is a single panel with a trigger:

```html
<ts-expansion-panel>
  <ts-expansion-panel-trigger>
    Here is my trigger!
  </ts-expansion-panel-trigger>

  <p>And here is my standard panel content.</p>
</ts-expansion-panel>
```

> NOTE: Without a trigger, the panel will not be visible.

#### Title and description

Trigger text can be split into `title` and `description` using the `TsExpansionPanelTitleComponent` and
`TsExpansionPanelDescriptionComponent` respectively.

```html
<!-- Standard trigger -->
<ts-expansion-panel-trigger>
  Here is my trigger!
</ts-expansion-panel-trigger>


<!-- Trigger with title and description -->
<ts-expansion-panel-trigger>
  <ts-expansion-panel-trigger-title>
    My title
  </ts-expansion-panel-trigger-title>

  <ts-expansion-panel-trigger-description>
    My description
  </ts-expansion-panel-trigger-description>
</ts-expansion-panel-trigger>
```

#### Disable a panel

The `isDisabled` flag will disable a panel and it's trigger:

```html
<ts-expansion-panel [isDisabled]="true">
  <ts-expansion-panel-trigger>
    Here is my trigger!
  </ts-expansion-panel-trigger>

  <p>I will never be seen.</p>
</ts-expansion-panel>
```

#### Default a panel open

The `isExpanded` flag will change the state of a panel. This can be used to default to a specific state or to dynamically change the state.

```html
<ts-expansion-panel [isExpanded]="true">
  <ts-expansion-panel-trigger>
    Here is my trigger!
  </ts-expansion-panel-trigger>

  <p>I'll be visible by default!</p>
</ts-expansion-panel>
```

#### Lazy loaded content

Panel content can be lazily loaded by using a template with the `tsExpansionPanelContent` directive. The template will not be loaded until
the panel is opened for the first time. The content will remain in the DOM until the panel is destroyed.

```html
<ts-expansion-panel>
  <ts-expansion-panel-trigger>
    Here is my trigger!
  </ts-expansion-panel-trigger>

  <ng-template tsExpansionPanelContent>
    Here is my deferred template!
  </ng-template>
</ts-expansion-panel>
```

#### Transparent mode

Expansion panel with transparent mode on has no box shadow and padding on the side. It's default to `false`.

```html
<ts-expansion-panel [transparentMode]="true">
  <ts-expansion-panel-trigger>
    Here is my trigger!
  </ts-expansion-panel-trigger>

  <p>And here is my standard panel content.</p>
</ts-expansion-panel>
```

#### Panel events

| Event            | Description                                        | Payload   |
|:-----------------|:---------------------------------------------------|:----------|
| `opened`         | Fired when the panel is opened                     | `void`    |
| `afterExpand`    | Fired after the panel expansion animation finishes | `void`    |
| `closed`         | Fired when the panel is closed                     | `void`    |
| `afterCollapse`  | Fired after the panel collapse animation finishes  | `void`    |
| `expandedChange` | Fired when the panel state changes                 | `boolean` |
| `destroyed`      | Fired when the panel is destroyed                  | `void`    |

```html
<ts-expansion-panel (opened)="myFunction()">...</ts-expansion-panel>
```

#### Custom trigger heights

Custom heights can be set for a trigger's collapsed and/or expanded state.

```html
<ts-expansion-panel>
  <!-- When collapsed the trigger will be 100px tall
       When expanded the trigger will be 200px tall -->
  <ts-expansion-panel-trigger
    collapsedHeight="100px"
    expandedHeight="200px"
  >Panel Trigger (100px -> 200px)</ts-expansion-panel-trigger>

  <p>And here is my standard panel content.</p>
</ts-expansion-panel>
```

#### Manual control

Panels can be programmatically opened, closed or toggled through a reference to the instance:

```typescript
@ViewChild(TsExpansionPanelComponent, {static: false})
public panel: TsExpansionPanelComponent;

...

panel.open();
panel.close();
panel.toggle();
```

> NOTE: Disabled panels cannot be controlled with these methods. Disabled panels can _only_ be controlled via the `isExpanded` input.

### Accordion

An accordion is created by wrapping two or more `TsExpansionPanelComponent`s inside a `TsAccordionComponent`.

```html
<ts-accordion>
  <ts-expansion-panel>...</ts-expansion-panel>
  <ts-expansion-panel>...</ts-expansion-panel>
</ts-accordion>
```

#### Allow multiple panels to be open

By default an accordion can only have a single panel open at a time. This functionality can be change with the `multi` input.

```html
<ts-accordion [multi]="true">
  <ts-expansion-panel>...</ts-expansion-panel>
  <ts-expansion-panel>...</ts-expansion-panel>
</ts-accordion>
```

#### Accordion events

| Event       | Description                           | Payload |
|:------------|:--------------------------------------|:--------|
| `destroyed` | Fired when the accordion is destroyed | `void`  |

```html
<ts-accordion (destroyed)="myFunction()">...</ts-accordion>
```

#### Accordion as a stepper

An accordion can function as a stepper which can be useful for guided flows. To facilitate this we can use a combination of `hideToggle` and
the `ts-expansion-panel-action-row`.

```html
<!-- Hide the toggle icon since this is a programmatically controlled flow -->
<ts-accordion [hideToggle]="true">
  <!-- STEP 1 -->
  <ts-expansion-panel [isExpanded]="activeStep === 0">
    <ts-expansion-panel-trigger>Step 1</ts-expansion-panel-trigger>

    And here is my standard panel content.

    <ts-expansion-panel-action-row>
      <ts-button (clicked)="nextStep()">Next</ts-button>
    </ts-expansion-panel-action-row>
  </ts-expansion-panel>

  <!-- STEP 2 -->
  <ts-expansion-panel [isExpanded]="activeStep === 1">
    <ts-expansion-panel-trigger>Step 2</ts-expansion-panel-trigger>

    And here is my standard panel content.

    <ts-expansion-panel-action-row>
      <ts-button format="hollow" (clicked)="previousStep()">Previous</ts-button>
      <ts-button (clicked)="nextStep()">Next</ts-button>
    </ts-expansion-panel-action-row>
  </ts-expansion-panel>

  <!-- STEP 3 -->
  <ts-expansion-panel [isExpanded]="activeStep === 2">
    <ts-expansion-panel-trigger>Step 3</ts-expansion-panel-trigger>

    And here is my standard panel content.

    <ts-expansion-panel-action-row>
      <ts-button format="hollow" (clicked)="previousStep()">Previous</ts-button>
      <ts-button (clicked)="nextStep()">End</ts-button>
    </ts-expansion-panel-action-row>
  </ts-expansion-panel>
</ts-accordion>
```

#### Hide toggle

When an accordion is controlled programmatically, the toggle icon can be hidden to avoid confusion for the user. Setting `hideToggle` on the
accordion will hide the toggle icon for *all panels within*.

> NOTE: This should _only_ be used in cases when the accordion is functioning as a stepper.

```html
<ts-accordion [hideToggle]="true">
  <ts-expansion-panel>...</ts-expansion-panel>
  <ts-expansion-panel>...</ts-expansion-panel>
</ts-accordion>
```

#### Action row

The action row is useful when an accordion is functioning as a stepper. Controls added within the action row will be right aligned as panel
controls.

> NOTE: See [Accordion as a stepper](https://github.com/GetTerminus/terminus-ui/blob/release/projects/library/expansion-panel/src/expansion-panel.component.md#accordion-as-a-stepper) for a complete example.

```html
<ts-expansion-panel>
  <ts-expansion-panel-trigger>
    Step 1
  </ts-expansion-panel-trigger>

  And here is my standard panel content.

  <ts-expansion-panel-action-row>
    <button (click)="nextStep()">Next</button>
  </ts-expansion-panel-action-row>
</ts-expansion-panel>
```

#### Open or close all panels

An accordion can programmatically open or close all panels at once.

```typescript
@ViewChild(TsAccordionComponent, {static: false})
public accordion: TsAccordionComponent;

...

accordion.openAll();
accordion.closeAll();
```

> NOTE: These methods will *not* change the state of disabled panels.

## Test Helpers

Some helpers are exposed to assist with testing. These are imported from `@terminus/ui-expansion-panel/testing`;

[[source]][test-helpers-src]

| Function                       |
|--------------------------------|
| `getAllPanelDebugElements`     |
| `getAllPanelInstances`         |
| `getPanelDebugElement`         |
| `getPanelInstance`             |
| `getPanelElement`              |
| `getPanelBodyElement`          |
| `getPanelBodyContentElement`   |
| `getAllAccordionDebugElements` |
| `getAllAccordionInstances`     |
| `getAccordionInstance`         |
| `getAccordionDebugElement`     |
| `getAccordionElement`          |
| `getTriggerDebugElement`       |
| `getTriggerInstance`           |
| `getTriggerElement`            |
| `getTriggerTitleElement`       |
| `getTriggerDescriptionElement` |
| `getPanelActionRow`            |
| `togglePanel`                  |

<!-- Links -->
[test-helpers-src]:    testing/src/test-helpers.ts
[license-url]:         https://github.com/GetTerminus/terminus-oss/blob/release/LICENSE
[license-image]:       http://img.shields.io/badge/license-MIT-blue.svg
[codecov-project]:     https://codecov.io/gh/GetTerminus/terminus-oss
[codecov-badge]:       https://codecov.io/gh/GetTerminus/terminus-oss/branch/release/graph/badge.svg
[npm-version-image]:   http://img.shields.io/npm/v/@terminus/ui-button.svg
[npm-package]:         https://www.npmjs.com/package/@terminus/ui-button
[github-action-badge]: https://github.com/GetTerminus/terminus-oss/workflows/Release%20CI/badge.svg
[github-action-link]:  https://github.com/GetTerminus/terminus-oss/actions?query=workflow%3A%22CI+Release%22
[file-size-badge]:     http://img.badgesize.io/https://unpkg.com/@terminus/ui-button/bundles/terminus-ui-button.umd.min.js?compression=gzip
[raw-distribution-js]: https://unpkg.com/@terminus/ui-button/bundles/terminus-ui-button.umd.js
