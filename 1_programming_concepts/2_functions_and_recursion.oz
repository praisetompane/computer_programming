%%% declare variale Fact
%%% create Facttin
   %%% and bound variable Fact to it
%%%  i.e. bound the identifier "Fact"
%%%         to the value : fun if N == 0 then 1 else {Fact N - 1} * N
declare
fun {Fact N}
   if N == 0 then 1 else {Fact N - 1}*N end
end

{Browse {Fact 10}}
{Browse {Fact 100}}
%%% The results of these invocations is known as infinite arbitary arithmetic
   %%% the inifinity is limited by the amout of memory the computer has

%%% math equivalient
   %%% 0! = 1
   %%% n! = n(n -)! if n > 0

%%% recursive becasuse, factorial of N is N times factorial of N - 1
%%% i.e. the concept of factorial references itself to complete itself
   %%%  i.e. defined in terms of itself