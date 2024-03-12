%%% def variable: 
%%%     shortcut to value
%%%     components:
%%%         the identifier := what you type in, what you use to refernce the value(i.e. store)
%%%         the store variable := this is what the system uses to calculate with
%%%                               part of system's memory, called its store
%%%         

%%% {} := procedure or function call
%%% Browse := one argument procedure
                %%% opens browser(i.e. window) and displays argumnet in it
%%% declare := creates a new store value
%%%            makes variable refer to the new store value
%%% An aside: previous calculations using the SAME identiifer do not change, 
%%%           because the identifier refers to another store variable
V=9999*9999
{Browse V}
