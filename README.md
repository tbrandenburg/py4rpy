# py4rpy

Python interface for IBM Rhapsody

## Dependencies

## Use cases

- Model-2-Model Transformation
- Model-2-text Transformation (code generation)
- Model checks

## Features

## Examples

### Build the project

1. Modify build.gradle providing correct rhapsody.jar file
    ~~~
    implementation files('c:/Program Files/IBM/Rhapsody/9.0.1/Share/JavaAPI/rhapsody.jar')
    ~~~
2. Run the build
    ~~~
    gradle build
    ~~~

### Run the JAR

~~~
java -Djava.library.path="c:/Program Files/IBM/Rhapsody/9.0.1/Share/JavaAPI/" -jar build/libs/py4rpy.jar
~~~
