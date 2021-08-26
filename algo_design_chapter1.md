
### 1)
>Decide whether you think the following statement is true or false. If it is true, give a short explanation. If it is false, give a counterexample.<p>
><i>True or false?  In every instance of the Stable Matching Problem, there is a stable matching containing a pair (m, w) such that m is ranked first on the preference list of w and w is ranked first on the preference list of m.</i>

**False.** Let us look at a counterexample. 

m preference list|m’ preference list|w preference list | w’ preference list
---|---|---|---|
w | w' | m' | m |
w'| w| m| m'  |

This is **an** instance of the Stable Matching Problem which results in (m, w) and (m’, w’). There are no instabilities because both m and m’ are matched with their first preference and have no incentive to leave their current partner. However, in this stable matching, the women are not with their first preference. So there is no pair (m, w) such that m is ranked first on w’s preference list. 

### 2)
>Decide whether you think the following statement is true or false. If it is true, give a short explanation. If it is false, give a counterexample.<p>
><i>True or false? Consider an instance of the Stable Matching Problem in which there exists a man m and a woman w such that m is ranked first on the preference list of w and w is ranked first on the preference list of m. Then in every stable matching S for this instance, the pair (m, w) belongs to S. </i>

**True.** Recall when men propose, they end up with their best valid partners (valid partner meaning they appear in some stable matching, best meaning it is the highest stable match in their preference list). 

Proof by contradiction:
m preference list|m’ preference list|w preference list | w’ preference list
---|---|---|---|
w | w | m | m |
w'| w'| m' | m'|

In the above example, suppose we had the pairs (m, w’) and (m’, w). <u>This would be an instability</u>
<br>
If m was rejected by a valid partner w, in favor of m’, then that m’ would need to be higher on w’s preference list - a contradiction.  <br>
If w is not matched with m, then that means that m never proposed and she had to settle for m’. That means that w was not first on the preference list of m - a contradiction. 
<br>
Since this is not the case, the pair (m, w) must belong to S.

### 3) 
>There are many other settings in which we can ask questions related to some type of “stability” principle. Here’s one, involving the competition between two enterprises. 
> Suppose we have two television networks, whom we’ll call A and B. There are n prime-time programming slots, and each network has n TV shows. Each network wants to devise a schedule—an assignment of each show to a distinct slot—so as to attract as much market share as possible.
> Here is the way we determine how well the two networks perform relative to each other, given their schedules. Each show has a fixed rating, which is based on the number of people who watched it last year; we’ll assume that no two shows have exactly the same rating. A network wins a given time slot if the show that it schedules for the time slot has a larger rating than the show the other network schedules for that time slot. The goal of each network is to win as many time slots as possible.
>Suppose in the opening week of the fall season, Network A reveals a schedule S and Network B reveals a schedule T. On the basis of this pair of schedules, each network wins certain time slots, according to the rule above. We’ll say that the pair of schedules (S, T) is stable if neither network can unilaterally change its own schedule and win more time slots. That is, there is no schedule S' such that Network A wins more slots with the pair (S', T) than it did with the pair (S, T); and symmetrically, there is no schedule T' such that Network B wins more slots with the pair (S, T') than it did with the pair (S, T).
>The analogue of Gale and Shapley’s question for this kind of stability is the following: For every set of TV shows and ratings, is there always a stable pair of schedules? Resolve this question by doing one of the following two things:
> (a) give an algorithm that, for any set of TV shows and associated ratings, produces a stable pair of schedules; or
> (b) give an example of a set of TV shows and associated ratings for which there is no stable pair of schedules.
