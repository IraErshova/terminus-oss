import threading
import queue
import time
import os
from pathlib import Path

def read_kbd_input(inputQueue):
    print('Input component name:')
    while (True):
        input_str = input()
        inputQueue.put(input_str)

def create(input):
  if not input or input == 'exit':
    print("no directory name provided. existing...")
    return
  # os.system('mkdir ui-%s' % input)
  try:
    Path("./ui/%s/schematics/ng-add" % input).mkdir(parents=True, exist_ok=False)
    print("Schematics directory created...")
    write_index(input)
    write_collection(input)
    write_tsconfig(input)
    update_package_json(input)
  except Exception as e:
    print('Failed : '+ str(e))

def write_index(input):
  print("Creating index.ts")
  file = open('ui/%s/schematics/ng-add/index.ts' % input, 'w+')
  file.write("import {"
             "\n  SchematicContext,"
             "\n  Tree,"
             "\n} from '@angular-devkit/schematics';"
             "\nimport { NodePackageInstallTask } from '@angular-devkit/schematics/tasks';"
             "\nimport {"
             "\n  addPackageJsonDependency,"
             "\n  NodeDependency,"
             "\n  NodeDependencyType,"
             "\n} from '@schematics/angular/utility/dependencies';"
             "\n"
             "\nexport const ngAdd = () => (tree: Tree, context: SchematicContext): Tree => {"
             "\n  ["
             "\n    '@angular/cdk: ^9.2.4',"
             "\n    '@angular/common: ^9.1.0',"
             "\n    '@angular/core: ^9.1.0',"
             "\n    '@angular/flex-layout: ~9.0.0-beta.29',"
             "\n    '@angular/forms: ^9.1.0',"
             "\n    '@angular/platform-browser: ^9.1.0',"
             "\n    '@terminus/design-tokens: ^2.0.2',"
             "\n    '@terminus/ngx-tools: ^8.0.5',"
             "\n    '@terminus/ui-utilities: ^1.0.0',"
             "\n    '@terminus/ui-%s: ^1.0.0',"
             "\n    'date-fns: ^2.14.0'"
             "\n  ].map(p => {"
             "\n    const individualPackage = p.split(':');"
             "\n    const nodeDependency: NodeDependency = {"
             "\n      type: NodeDependencyType.Default,"
             "\n      name: individualPackage[0],"
             "\n      version: individualPackage[1],"
             "\n      overwrite: false,"
             "\n    };"
             "\n    addPackageJsonDependency(tree, nodeDependency);"
             "\n    context.logger.info("
             "\n      `✅️ Added dependency: ${individualPackage[0]}@${"
             "\n        individualPackage[1]"
             "\n      }`,"
             "\n    );"
             "\n    context.addTask(new NodePackageInstallTask());"
             "\n  });"
             "\n  return tree;"
             "\n};" % input
  )
  file.close()

def write_collection(input):
  print("Creating collection.json...")
  file = open('ui/%s/schematics/collection.json' % input, 'w+')
  file.write('{'
             '\n  "$schema": "../../../../node_modules/@angular-devkit/schematics/collection-schema.json",'
             '\n  "schematics": {'
             '\n    "ng-add": {'
             '\n      "description": "Add required package to the module.",'
             '\n      "factory": "./ng-add/index#ngAdd"'
             '\n    }'
             '\n  }'
             '\n}')
  file.close()

def write_tsconfig(input):
  print("Creating tsconfig.schematics.json...")
  file = open('ui/%s/tsconfig.schematics.json' % input, 'w+')
  file.write('{'
             '\n  "compilerOptions": {'
             '\n    "resolveJsonModule": true,'
             '\n    "esModuleInterop": true,'
             '\n    "baseUrl": ".",'
             '\n    "lib": ['
             '\n      "es2018",'
             '\n      "dom"'
             '\n    ],'
             '\n    "declaration": true,'
             '\n    "module": "commonjs",'
             '\n    "moduleResolution": "node",'
             '\n    "noEmitOnError": true,'
             '\n    "noFallthroughCasesInSwitch": true,'
             '\n    "noImplicitAny": true,'
             '\n    "noImplicitThis": true,'
             '\n    "noUnusedParameters": true,'
             '\n    "noUnusedLocals": true,'
             '\n    "rootDir": "schematics",'
             '\n    "outDir": "../../../dist/libs/ui/%s/schematics",'
             '\n    "skipDefaultLibCheck": true,'
             '\n    "skipLibCheck": true,'
             '\n    "sourceMap": true,'
             '\n    "strictNullChecks": true,'
             '\n    "target": "es6",'
             '\n    "types": ['
             '\n      "jest",'
             '\n      "node"'
             '\n    ]'
             '\n  },'
             '\n  "include": ['
             '\n    "schematics/**/*"'
             '\n  ],'
             '\n  "exclude": ['
             '\n    "schematics/*/files/**/*"'
             '\n  ]'
             '\n}' % input)
  file.close()

def update_package_json(input):
  print("Updating package.json...")
  print("./ui/{}/package.json".format(input))
  file = open('./ui/{}/package.json'.format(input), "r")
  contents = file.readlines()
  print("content read..")
  index = len(contents) - 2
  contents[index] = contents[index].replace('\n', ',\n', 1)
  contents = "".join(contents)

  file.close()

  file = open('./ui/{}/package.json'.format(input), "w+")
  file.write(contents)
  file.close()

  file = open('./ui/{}/package.json'.format(input), "r")
  contents = file.readlines()
  file.close()

  value = '  "scripts": {\n    "build": "../../../node_modules/.bin/tsc -p tsconfig.schematics.json",\n    "copy:collection": "cp schematics/collection.json ../../../dist/libs/ui/%s/schematics/collection.json",\n    "postbuild": "npm run copy:collection"\n  },\n  "schematics": "./schematics/collection.json"\n' % input
  contents.insert(index+1, value)

  print("Opening package.json to write...")
  file = open('./ui/{}/package.json'.format(input), "w+")
  contents = "".join(contents)
  file.write(contents)
  print("Done writing...")
  file.close()

def move_spec(input):
  print("move spec here")
  command = 'find ../libs -name "{}*.spec.ts"'.format(input)
  f = os.popen(command)
  find = f.read()
  os.popen('mv {} ./ui-{}'.format(find.strip(), input))


def main():
    EXIT_COMMAND = "exit"
    inputQueue = queue.Queue()

    inputThread = threading.Thread(target=read_kbd_input, args=(inputQueue,), daemon=True)
    inputThread.start()

    while (True):
        if (inputQueue.qsize() > 0):
            input_str = inputQueue.get()

            print("input_str = {}".format(input_str))

            if (input_str == EXIT_COMMAND):
                print("Exiting serial terminal.")
                break

            # Insert your code here to do whatever you want with the input_str.
            create(input_str)

        # The rest of your program goes here.

        time.sleep(0.01)
    print("End.")

if (__name__ == '__main__'):
    main()
