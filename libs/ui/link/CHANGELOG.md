# Change Log

All notable changes to this project will be documented in this file.
See [Conventional Commits](https://conventionalcommits.org) for commit guidelines.

## [2.1.2](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@2.1.1...@terminus/ui-link@2.1.2) (2020-09-14)

**Note:** Version bump only for package @terminus/ui-link





## [2.1.1](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@2.1.0...@terminus/ui-link@2.1.1) (2020-09-11)

**Note:** Version bump only for package @terminus/ui-link





# [2.1.0](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@2.0.15...@terminus/ui-link@2.1.0) (2020-09-08)


### Features

* clean all markdown ([5249a59](https://github.com/GetTerminus/terminus-oss/commit/5249a59486be63b6d9a0be7a801defb9b6adcedc))





## [2.0.15](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@2.0.14...@terminus/ui-link@2.0.15) (2020-09-04)

**Note:** Version bump only for package @terminus/ui-link





## [2.0.14](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@2.0.13...@terminus/ui-link@2.0.14) (2020-09-03)

**Note:** Version bump only for package @terminus/ui-link

## [2.0.13](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@2.0.12...@terminus/ui-link@2.0.13) (2020-08-27)

**Note:** Version bump only for package @terminus/ui-link

## [2.0.12](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@2.0.11...@terminus/ui-link@2.0.12) (2020-08-21)

### Bug Fixes

* **Link:** fix style regression for links inside menu panels ([b8161c9](https://github.com/GetTerminus/terminus-oss/commit/b8161c91c945c96cf80792ae7f3765cd081d597c)), closes [#280](https://github.com/GetTerminus/terminus-oss/issues/280)

## [2.0.11](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@2.0.10...@terminus/ui-link@2.0.11) (2020-08-14)

**Note:** Version bump only for package @terminus/ui-link

## [2.0.10](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@2.0.9...@terminus/ui-link@2.0.10) (2020-08-10)

### Bug Fixes

* **Link:** updated icon size ([d381dff](https://github.com/GetTerminus/terminus-oss/commit/d381dff3a04f4a586ee0c4c4e23ab7334400bb63))

## [2.0.9](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@2.0.8...@terminus/ui-link@2.0.9) (2020-08-10)

**Note:** Version bump only for package @terminus/ui-link

## [2.0.8](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@2.0.7...@terminus/ui-link@2.0.8) (2020-08-10)

**Note:** Version bump only for package @terminus/ui-link

## [2.0.7](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@2.0.6...@terminus/ui-link@2.0.7) (2020-08-10)

**Note:** Version bump only for package @terminus/ui-link

## [2.0.6](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@2.0.5...@terminus/ui-link@2.0.6) (2020-08-06)

### Bug Fixes

* **Link:** more lps tweaks ([48b1fd3](https://github.com/GetTerminus/terminus-oss/commit/48b1fd3f95d15387aec2e3bf0a847748ffb3f297))

## [2.0.5](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@2.0.4...@terminus/ui-link@2.0.5) (2020-07-31)

**Note:** Version bump only for package @terminus/ui-link

## [2.0.4](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@2.0.3...@terminus/ui-link@2.0.4) (2020-07-30)

### Bug Fixes

* more LPS tweaks ([dedfcf9](https://github.com/GetTerminus/terminus-oss/commit/dedfcf947e3bcd33041b388ccab9bcc5bf273f51))

## [2.0.3](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@2.0.2...@terminus/ui-link@2.0.3) (2020-07-29)

**Note:** Version bump only for package @terminus/ui-link

## [2.0.2](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@2.0.1...@terminus/ui-link@2.0.2) (2020-07-28)

**Note:** Version bump only for package @terminus/ui-link

## [2.0.1](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@2.0.0...@terminus/ui-link@2.0.1) (2020-07-28)

### Bug Fixes

* bump all package versions ([9446c0d](https://github.com/GetTerminus/terminus-oss/commit/9446c0d5cde3bd693cfba7cabbfd2db443a47b00))

## 2.0.0 (2020-07-27)

### Bug Fixes

* **Link:** Update link styles for LPS ([7b20b00](https://github.com/GetTerminus/terminus-oss/commit/7b20b0063c107d343cf9bcd276db02c863566012)), closes [#32](https://github.com/GetTerminus/terminus-oss/issues/32)

### BREAKING CHANGES

* **Link:** Link styles changed

#### 2.0.0 Migration Notes

##### CSS Resources

Remove any imports or `<link>` tags importing Material Icons:

```diff
-<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
```

Update the imported font families:

```diff
-<link href="https://fonts.googleapis.com/css?family=Roboto:400,500,700" rel="stylesheet">
+<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
```

##### Theme

No longer accepts the `theme` input:

```diff
-<ts-link theme="primary">My link</ts-link>
+<ts-link>My link</ts-link>
```

## 1.0.15 (2020-07-13)

**Note:** Version bump only for package @terminus/ui-link

## [1.0.14](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@1.0.13...@terminus/ui-link@1.0.14) (2020-07-07)

**Note:** Version bump only for package @terminus/ui-link

## [1.0.13](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@1.0.12...@terminus/ui-link@1.0.13) (2020-06-30)

### Bug Fixes

* **Link:** trigger release ([b269746](https://github.com/GetTerminus/terminus-oss/commit/b2697467a533c3f87e4d04a1fb44798b40b71c72))

## [1.0.12](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@1.0.11...@terminus/ui-link@1.0.12) (2020-06-30)

### Bug Fixes

* **Link:** trigger release ([2c9632a](https://github.com/GetTerminus/terminus-oss/commit/2c9632afcf7e59a19d47f119d93b34f17c19c4f3))

## [1.0.11](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@1.0.10...@terminus/ui-link@1.0.11) (2020-06-30)

### Bug Fixes

* **Link:** trigger release ([7f7de2d](https://github.com/GetTerminus/terminus-oss/commit/7f7de2ddf13821330bd7f7011d748db917d86d6b))

## [1.0.10](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@1.0.9...@terminus/ui-link@1.0.10) (2020-06-30)

### Bug Fixes

* **Link:** enforce noopener for external links ([03b406a](https://github.com/GetTerminus/terminus-oss/commit/03b406a68163aca1574945f39d6e6fe5106764cf)), closes [#131](https://github.com/GetTerminus/terminus-oss/issues/131)

## 1.0.9 (2020-06-23)

**Note:** Version bump only for package @terminus/ui-link

## [1.0.8](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@1.0.4...@terminus/ui-link@1.0.8) (2020-06-11)

### Bug Fixes

* **Link:** trigger release ([8b45432](https://github.com/GetTerminus/terminus-oss/commit/8b454327a84acd6903309f3fd04719796e17ca69))

### Reverts

* **Link:** incorrect version bump ([ad02882](https://github.com/GetTerminus/terminus-oss/commit/ad02882b608334be8023c23d8102b65c8e223e02))

## [1.0.7](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@1.0.4...@terminus/ui-link@1.0.7) (2020-06-11)

### Bug Fixes

* **Link:** trigger release ([8b45432](https://github.com/GetTerminus/terminus-oss/commit/8b454327a84acd6903309f3fd04719796e17ca69))

### Reverts

* **Link:** incorrect version bump ([ad02882](https://github.com/GetTerminus/terminus-oss/commit/ad02882b608334be8023c23d8102b65c8e223e02))

## [1.0.6](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@1.0.4...@terminus/ui-link@1.0.6) (2020-06-11)

### Bug Fixes

* **Link:** trigger release ([8b45432](https://github.com/GetTerminus/terminus-oss/commit/8b454327a84acd6903309f3fd04719796e17ca69))

### Reverts

* **Link:** incorrect version bump ([ad02882](https://github.com/GetTerminus/terminus-oss/commit/ad02882b608334be8023c23d8102b65c8e223e02))

## [1.0.5](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@1.0.4...@terminus/ui-link@1.0.5) (2020-06-11)

### Bug Fixes

* **Link:** trigger release ([927ab45](https://github.com/GetTerminus/terminus-oss/commit/927ab4512804f4a7ebe4b39a26f212ec9bf411f1))

## [1.0.4](https://github.com/GetTerminus/terminus-oss/compare/@terminus/ui-link@1.0.3...@terminus/ui-link@1.0.4) (2020-06-10)

### Bug Fixes

* **Link:** trigger release ([91cbac8](https://github.com/GetTerminus/terminus-oss/commit/91cbac890e66d7cf8a679646f449579b3583c166))

## 1.0.3 (2020-06-10)

### Bug Fixes

* bump all internal dependencies ([ff26b80](https://github.com/GetTerminus/terminus-oss/commit/ff26b806bb599401f006996be5b567a378e68ef3))

## 1.0.2 (2020-06-09)

### Bug Fixes

* **Button:** update ([a47f307](https://github.com/GetTerminus/terminus-oss/commit/a47f30757b9216d6ee76788c117e76eacf5289e5))
