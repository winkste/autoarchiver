# autoarchiver
A python program to automatically archive files from a temporary folder to a backup folder including log file

## Setup the development environment
tbd
### Virtual Environment
tbd
### Pylint
tbd
### Unit Testing using pytest
tbd
### Call the program
tbd

## General flow of control
This chapter gives a short introduction how the program control flow looks like.

``` mermaid
graph TD
    A(Start)
    B{parameter check}
    C[create list of files]
    D[filter list of files by date]
    E[archive files]
    F[create archive log file]
    G[move archived files to trash]
    Z(End)

    A-->B
    B-->|param valid|C
    B-->|param not valid|Z
    C-->D
    D-->E
    E-->F
    F-->G
    G-->Z
    
```

