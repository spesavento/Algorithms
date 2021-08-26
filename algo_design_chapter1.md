
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
>There are many other settings in which we can ask questions related to some type of “stability” principle. Here’s one, involving the competition between two enterprises. <p>
> Suppose we have two television networks, whom we’ll call A and B. There are n prime-time programming slots, and each network has n TV shows. Each network wants to devise a schedule—an assignment of each show to a distinct slot—so as to attract as much market share as possible.<p>
> Here is the way we determine how well the two networks perform relative to each other, given their schedules. Each show has a fixed rating, which is based on the number of people who watched it last year; we’ll assume that no two shows have exactly the same rating. A network wins a given time slot if the show that it schedules for the time slot has a larger rating than the show the other network schedules for that time slot. The goal of each network is to win as many time slots as possible.<p>
>Suppose in the opening week of the fall season, Network A reveals a schedule S and Network B reveals a schedule T. On the basis of this pair of schedules, each network wins certain time slots, according to the rule above. We’ll say that the pair of schedules (S, T) is stable if neither network can unilaterally change its own schedule and win more time slots. That is, there is no schedule S' such that Network A wins more slots with the pair (S', T) than it did with the pair (S, T); and symmetrically, there is no schedule T' such that Network B wins more slots with the pair (S, T') than it did with the pair (S, T).<p>
>The analogue of Gale and Shapley’s question for this kind of stability is the following: For every set of TV shows and ratings, is there always a stable pair of schedules? Resolve this question by doing one of the following two things:<p>
> (a) give an algorithm that, for any set of TV shows and associated ratings, produces a stable pair of schedules; or<p>
> (b) give an example of a set of TV shows and associated ratings for which there is no stable pair of schedules.

There is not always a stable pair of schedules. Suppose Network A has two shows {a1, a2} with ratings 20 and 40. Network B has two shows {b1, b2} with ratings 10 and 30. 

Each network can reveal two scedules (total of 2x2 = 4, but for the following if both swapped it'd be the same situation/dilemma):

<span style="color:cornflowerblue">*Unstable: If this schedule came out, Network A would get two slots and Network B would get 0. In this case, Network B would want to swap it's shows so that 30 > 20 and it gets 1 slot instead of 0. </span>
|A  | B|     
|---|---|
|20 |10  |
|40 |30  | 

<span style="color:cornflowerblue">*Unstable: If this schedule came out, Network A would get 1 slot and Network B would get 1 slot. In this case, Network A would want to swap it's shows so that 40 > 30 and 20 > 10 and it gets 2 slots instead of 1. </span>
|A  | B|
|---|---|
|20 |30  |
|40 |10  |

### 4) 
> Gale and Shapley published their paper on the Stable Matching Problem in 1962; but a version of their algorithm had already been in use for ten years by the National Resident Matching Program, for the problem of assigning medical residents to hospitals.<p>
> Basically, the situation was the following. There were m hospitals, each with a certain number of available positions for hiring residents. There were n medical students graduating in a given year, each interested in joining one of the hospitals. Each hospital had a ranking of the students in order of preference, and each student had a ranking of the hospitals in order of preference. We will assume that there were more students graduating than there were slots available in the m hospitals.<p>
> The interest, naturally, was in finding a way of assigning each student to at most one hospital, in such a way that all available positions in all hospitals were filled. (Since we are assuming a surplus of students, there would be some students who do not get assigned to any hospital.)<p>
> We say that an assignment of students to hospitals is stable if neither of the following situations arises.<br>
> First type of instability: There are students s and s', and a hospital h, so that
> * s is assigned to h, and
> * s' is assigned to no hospital, and
> * h prefers s' to s.

>Second type of instability: There are students s and s', and hospitals h and h', so that
> * s is assigned to h, and
> * s' is assigned to h', and
> * h prefers s' to s, and
> * s' prefers h to h'.

> So we basically have the Stable Matching Problem, except that (i) hospitals generally want more than one resident, and (ii) there is a surplus of medical students.
> Show that there is always a stable assignment of students to hospitals, and give an algorithm to find one.

Have hopsitals h and h' rank their student preferences. Have students rank their hospital preferences.

<span style="font-family:Courier;">
while there is a hospital hi that has available positions:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;accept the first student si on it's preference list<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if the student si is free/unmatched:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; student si accepts the offer<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else student already accepted hospital hk:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if student si prefers hospital hk to hi:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reject hi and remain commited to hk<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else si revokes their offer and joins hopsital hi:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# of available positions at hospital hk increases by one<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$ of available positions at hospital hi decreases by one<br> 
</span>


### 5) 
### 6) 
### 7) 
### 8) 
