#! /bin/bash

unset IS_C
unset IS_PYTHON

usage() {
  echo "Usage: new.sh [-h, -p | -c] <type>/<filename>"
  echo "Creates a new file in the current directory"
  echo "Options:"
  echo " -h Show this help message"
  echo " -p To create a python file"
  echo " -c To create a C file"
  exit 1
}


if [ $# -lt 1 ]; then
  usage
  exit 1
fi


python_file() {
  DIR=./$TYPE/$FILENAME
  mkdir -p $DIR
  FILE=$DIR/$FILENAME.py
  touch $FILE
  cat > $FILE <<EOF
#! /bin/python3

def main():
    return


if __name__ == "__main__":
    main()
EOF
}

c_file() {
  DIR=./$TYPE/$FILENAME
  mkdir -p $DIR
  FILE=$DIR/$FILENAME.c
  touch $FILE
  cat > $FILE <<EOF
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  return 0;
}
EOF
}


main() {
  POSITIONAL_ARGS=()

  while [[ $# -gt 0 ]]; do
    case $1 in
      -h)
        usage
        exit 1
      ;;
      -p)
        IS_PYTHON=true
        shift
      ;;
      -c) 
        IS_C=true
        shift
      ;;
      -*) 
        echo "Unknown option: $1"
        usage
        exit 1
      ;;
      *)
        POSITIONAL_ARGS+=("$1")
        shift 
      ;;
    esac
  done

  PATH_TO_FILE=${POSITIONAL_ARGS[0]}
  FILE_ARR=(${PATH_TO_FILE//\// })
  TYPE=${FILE_ARR[0]}
  FILENAME=${FILE_ARR[1]}

  if [ -z $IS_C ] ; then
    python_file
  elif [ -z $IS_PYTHON ] ; then
    c_file
  else
    echo "No file type specified"
    echo "Creating a Python File at ./$TYPE/$FILENAME/$FILENAME.py"
    python_file
  fi
}

main $@