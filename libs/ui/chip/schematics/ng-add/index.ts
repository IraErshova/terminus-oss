import {
  SchematicContext,
  Tree,
} from '@angular-devkit/schematics';
import { NodePackageInstallTask } from '@angular-devkit/schematics/tasks';
import {
  addPackageJsonDependency,
  NodeDependency,
  NodeDependencyType,
} from '@schematics/angular/utility/dependencies';
import { get } from 'http';
import { of } from 'rxjs';
import {
  concatMap,
  map,
} from 'rxjs/operators';


export const ngAdd = () => (tree: Tree, _context: SchematicContext) => of(
  '@angular/cdk',
  '@angular/material',
  '@terminus/design-tokens',
  '@terminus/ngx-tools',
  '@terminus/ui-chip',
  '@terminus/ui-icon',
  '@terminus/ui-utilities',
  '@terminus/ui-styles',
  'date-fns',
).pipe(
  concatMap(name => getLatestNodeVersion(name)),
  map(npmRegistryPackage => {
    const nodeDependency: NodeDependency = {
      type: NodeDependencyType.Default,
      name: npmRegistryPackage.name,
      version: npmRegistryPackage.version,
      overwrite: false,
    };
    addPackageJsonDependency(tree, nodeDependency);
    _context.logger.info(`✅️ Added dependency: ${npmRegistryPackage.name}@${
      npmRegistryPackage.version
    }`);
    _context.addTask(new NodePackageInstallTask());
    return tree;
  }),
);

export interface NpmRegistryPackage {
  name: string;
  version: string;
}

/**
 * @param packageName
 */
export function getLatestNodeVersion(
  packageName: string,
): Promise<NpmRegistryPackage> {
  const DEFAULT_VERSION = 'latest';
  /**
   * @param name
   * @param version
   */
  const buildPackage = (
    name: string,
    version: string = DEFAULT_VERSION,
  ): NpmRegistryPackage => ({ name,
    version });

  return new Promise(resolve => get(`http://registry.npmjs.org/${packageName}`, res => {
    let rawData = '';
    res.on('data', chunk => (rawData += chunk));
    res.on('end', () => {
      try {
        const response = JSON.parse(rawData);
        const version = (response && response['dist-tags']) || {};

        resolve(buildPackage(response.name || packageName, version.latest));
      } catch (e) {
        resolve(buildPackage(packageName));
      }
    });
  }).on('error', () => resolve(buildPackage(packageName))));


}

