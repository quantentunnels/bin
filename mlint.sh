#!/bin/bash
# wraper for the MATLAB mlint code checker

# arguments
# '-m2'         % errors only
# '-m1'         % errors and severe warnings only
# '-m0'         % all errors and warnings

/usr/local/MATLAB/R2015a/bin/glnxa64/mlint "$@"


## undocumented mlint fatures form Yair Altmans ##
# [http://undocumentedmatlab.com/blog/parsing-mlint-code-analyzer-output](Undocumented MATLAB)
# '-all'        % ???
# '-allmsg'     % display the full list of possible mlint messages and their codes
# '-amb'        % display all possibly-ambiguous identifiers (variable/function)
# '-body'       % ???
# '-callops'    % display the internal call tree, with nesting levels and function types
# '-calls'      % (looks similar to -callops, not sure what the difference is)
# '-com'        % ???
# '-cyc'        % display McCabe complexity value of all functions in the analyzed file
# '-db'         % == -set + -ud + -tab
# '-dty'        % debug info for the mlint parsing tree
# '-edit'       % display all encountered identifiers and their assumed types
# '-en'         % messages in English
# '-id'         % display the mlint code associated with each message
# '-ja'         % messages in Japanese
# '-lex'        % display the LEX parse-tree for the analyzed file
# '-m0'         % + other opt
# '-m1'         % + other opt
# '-m2'         % + other opt
# '-m3'         % + other opt
# '-mess'       % debug info for mlint message-reporting (start/end locations etc.)
# '-msg'        % (looks similar to -allmsg above, not sure what the difference is)
# '-notok'      % disregard %#ok directives and report messages on lines having them
# '-pf'         % ???
# '-set'        % debug info for the mlint parsing tree
# '-spmd'       % ??? (presumably display SPMD-related messages)
# '-stmt'       % display the number of statements in each function within the analyzed file
# '-tab'        % set-by/used-by table for all identifiers (see -edit)
# '-tmtree'     % not valid anymore
# '-tmw'        % not valid anymore
# '-toks'       % ???
# '-tree'       % debug info for the mlint parsing tree
# '-ty'         % display the line numbers where each of the file's identifiers are used
# '-ud'         % debug info for the mlint parsing tree
# '-yacc'       % ONLY: !mlint FILE -yacc -...
