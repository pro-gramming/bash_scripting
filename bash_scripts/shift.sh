#!/bin/bash

# using the concept of shift

while (( $# ))
	do
		echo "you gave me $1"
		shift
	done

