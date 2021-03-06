
### 1)
>Decide whether you think the following statement is true or false. If it is true, give a short explanation. If it is false, give a counterexample.<p>
><i>True or false?  In every instance of the Stable Matching Problem, there is a stable matching containing a pair (m, w) such that m is ranked first on the preference list of w and w is ranked first on the preference list of m.</i>

**False.** Let us look at a counterexample. 

m preference list|m’ preference list|w preference list | w’ preference list
---|---|---|---|
w | w' | m' | m |
w'| w| m| m'  |

This is **an** instance of the Stable Matching Problem which results in (m, w) and (m’, w’). There are no instabilities because both m and m’ are matched with their first preference and have no incentive to leave their current partner. However, in this stable matching, the women are not with their first preference. So there is no pair (m, w) such that w is ranked first on m’s preference list and m is ranked first on w’s preference list.

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

Have hospitals h and h' rank their student preferences. Have students rank their hospital preferences.

At any point in time, a student is either committed to a hospital or free. A hospital either has available positions or is full. 

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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# of available positions at hospital hi decreases by one<br> 
</span>

If there are m hospitals and n students, then the algorithm will terminate in O(mn) steps because each hospital offers a position to a student at most once, and in each iteration, some hospital offers a position to some student. The algorithm terminates when all positions (p) are filled, since they must offer one to every student and p < n. 
<br>
Let us argue that the assignment is stable by looking at the two forms of instability. <br>
1) Instability 1 involves a case where s is assigned to h, but h prefers s' and s' is assigned to no hospital. This cannot happen, as if h prefers s', then h must have accepted s' first before s. In that case, s' would have accepted a position for some hospital and it would not be free (either hopsital h or it might have accepted another hospital that ranked higher for it) - a contradiction. 
2) Instability 2 involves when s is assigned to h and s' is assigned to h'. h prefers s' to s and s' prefers h to h'. This cannot happen because if h prefers s' to s, it must have extended an offer to it before s. That means at some point s' turned down h for a hospital that was higher ranking on its preference list. Therefore s' cannot prefer h to its current match. - this is a contradiction.

### 5) 
>The Stable Matching Problem, as discussed in the text, assumes that all men and women have a fully ordered list of preferences. In this problem we will consider a version of the problem in which men and women can be indifferent between certain options. As before we have a set M of n men and a set W of n women. Assume each man and each woman ranks the members of the opposite gender, but now we allow ties in the ranking. For example (with n = 4), a woman could say that m1 is ranked in first place; second place is a tie between m2 and m3 (she has no preference between them); and m4 is in last place. We will say that w prefers m to m' if m is ranked higher than m' on her preference list (they are not tied). <p>
>With indifferences in the rankings, there could be two natural notions for stability. And for each, we can ask about the existence of stable matchings, as follows.<p>
> **a)** A strong instability in a perfect matching S consists of a man `m` and a woman `w`, such that each of `m` and `w` prefers the other to their partner in S. Does there always exist a perfect matching with no strong instability? Either give an example of a set of men and women with preference lists for which every perfect matching has a strong instability; or give an algorithm that is guaranteed to find a perfect matching with no strong instability.

**Yes**. Let us break ties lexographically. If man m is indifferent between wi and wj, then say wi appears first on the preference list cause (i < j). If woman w is indifferent between mi and mj, then mi appears first on their preference list since (i < j).<br>
Now if we run the stable matching algorihtm with these concrete preference lists, we know that this algorihtm produces a stable matching - a matching with no instabilities. 

> **b)** A weak instability in a perfect matching s consists of a man m and a woman w, such that their partners in S are w' and m', respectively, and one of the following holds:
> - `m` prefers `w` to `w'`, and `w` either prefers `m` to `m'` or is indifferent between these two choices; or
> - `w` prefers `m` to `m'`, and `m` either prefers `w` to `w'` or is indifferent between these two choices.

> In other words, the pairing between `m` and `w` is either preferred by both, or preferred by one while the other is indifferent. Does there **always** exist a perfect matching with no weak instability? Either give an example of a set of men and women with preference lists for which every perfect matching has a weak instability; or give an algorithm that is guaranteed to find a perfect matching with no weak instability.

**No**. Say m prefers w to w', and also m' prefers w to w'. And w is tied between m and m', no preference. Then we could end up with the following matches:<br>
- We end up with pairs (m, w) and (m', w'). Here m got his first pick, but m' did not. We have a case where we have a weak instability. 
- We end up with pairs (m, w') and (m', w). Here m' got his first pick, but m did not. We have a case where we have a weak instability. 

### 6) 
>Peripatetic Shipping lines, Inc., is a shipping company that owns n ships and provides service to n ports. Each of its ships has a schedule that says, for each day of the month, which of the ports it's currently visiting, or whether it's out at sea. (You can assume the "month" here has m days, for some m > n.) Each ship visits each port for exactly one day during the month. For safety reasons, PSL Inc. has the following strict requirement:<p>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(t) No two ships can be in the same port on the same day.<p>
>The company wants to perform maintenance on all the ships this month, via the following scheme. They want to truncate each ship's schedule: for each ship Si, there will be some day when it arrives in its scheduled port and simply remains there for the rest of the month (for maintenance). This means that Si will not visit the remaining ports on its schedule (if any) that month, but this is okay. So the truncation of Si's schedule will simply consist of its original schedule up to a certain specified day on which it is in a port P; the remainder of the truncated schedule simply has it remain in port P.<p>
> Now the company's question to you is the following: Given the schedule for each ship, find a truncation of each so that condition (t) continues to hold: no two ships are ever in the same port on the same day.<p>
> Show that such a set of truncations can always be found, and give an algorithm to find them. <p>
> **Example.** Suppose we have two ships and two ports, and the "month" has four days. Suppose the first ship's schedule is <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>port P1; at sea; port P2; at sea</i><br>
> and the second ship's schedule is <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>at sea; port P1; at sea; port P2 .</i><br>
> Then the (only) way to choose truncations would be to have the first ship remain in port P2 starting on day 3, and have the second ship remain in port P1 starting on day 2.

Each ship ranks the ports it visits in chronological order (first at the top). Each port ranks the ships that visit it in reverse chronological order. Here is a visualization of why we do reverse order here:<br>

Ship A - port P1; at sea; port P2; at sea <br>
Ship B - at sea; port P1; at sea; port P2 <br>

Ship A&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ship B<br>
P1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;P1<br>
P2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;P2 <br>

P1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;P2<br>
Ship B&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ship B&nbsp;&nbsp;&nbsp;&nbsp;*B coming in later after time at sea<br>
Ship A&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ship A<br>

Now, as the Stable Matching Problem goes, Ship A goes for it's top choice, P1. P1 accepts it because the port is free. Ship B comes in to it's top choice, P1. Now P1 prefers Ship B because it came in later, and Ship A tries for the second in it's list, P2. P2 accepts Ship A because it is free.

We can prove that a stable matching between ships and ports defines an acceptable assingment of stopping ports. If the assignment is not acceptable, then it violates condition (t). That is, some ship Si passes through port Pk after ship Sj has already stopped there. But in this case, under our preference relation above, ship Si "prefers" Pk to its actual stopping port, and port Pk "prefers" ship Si to ship Sj. This contradicts the assumption that we chose a stable matching between ships and ports.


### 7) 
>Some of your friends are working for CluNet, a builder of large commu- nication networks, and they are looking at algorithms for switching in a particular type of input/output crossbar. <p>
>Here is the setup. There are n input wires and n output wires, each directed from a source to a terminus. Each input wire meets each output wire in exactly one distinct point, at a special piece of hardware called a junction box. Points on the wire are naturally ordered in the direction from source to terminus; for two distinct points x and y on the same wire, we say that x is <u>upstream</u> from y if x is closer to the source than y, and otherwise we say x is <u>downstream</u> from y. The order in which one input wire meets the output wires is not necessarily the same as the order in which another input wire meets the output wires. (And similarly for the orders in which output wires meet input wires.) Figure 1.8 gives an example of such a collection of input and output wires. <p>
>Now, here's the switching component of this situation. Each input wire is carrying a distinct data stream, and this data stream must be switched onto one of the output wires. If the stream of Input i is switched onto Output j, at junction box B, then this stream passes through all junction boxes upstream from B on Input i, then through B, then through all junction boxes downstream from B on Output j. It does not matter which input data stream gets switched onto which output wire, but each input data stream must be switched onto a different output wire. Furthermore-and this is the tricky constraint-no two data streams can pass through the same junction box following the switching operation. <p>
>Finally, here's the problem. Show that for any specified pattern in which the input wires and output wires meet each other (each pair meeting exactly once), a valid switching of the data streams can always be found-one in which each input data stream is switched onto a different output, and no two of the resulting streams pass through the same junction box. Additionally, give an algorithm to find such a valid switching.

<img src="./Images/Figure_1_8.png" alt="drawing" width="500"/>

This problem is quite similar to the previous problem with ships and ports.<br>
An **input wire** wants its data stream to be switched as early (close to the source) as possible, in order to minimize its risk of running into another data stream that has already been switched, at the junction box. <br>
An **output wire** wants its data stream to be switched as late (far from the source) as possible, in order to minimize its risk of running into another data stream, that has not yet been switched, at a junction box. <p>
For our Stable Matching Problem, each wire ranks the output wires in the order it encounters them - from source to terminus. Each output wire ranks the input wires in the reverse of the order it encounters them from source to terminus. 
<p>
Suppose we have Input i and Output j that meet at a junction box. Then one stream originates on Input i, and the other must have switched from a different input wire, say Input k, onto Output j.<br>
However, in this case Output j prefers Input i to Input k (since j meets i downstream from k), and Input i prefers Output j to, say, Output l (since Input i meets Output j upstream from Output l). This contradicts the assumption that we chose a stable matching between input wires and output wires.
<p>
Note: Creating preference lists for stable matchings will take O(n^2), as will computing the stable matching.

### 8) 
> For this problem, we will explore the issue of truthfulness in the Stable Matching Problem and specifically in the Gale-Shapley algorithm. The basic question is: Can a man or a woman end up better off by lying about his or her preferences? More concretely, we suppose each participant has a true preference order. Now consider a woman w. Suppose w prefers man m to m', but both m and m' are low on her list of preferences. Can it be the case that by switching the order of m and m' on her list of preferences (i.e., by falsely claiming that she prefers m' to m) and running the algorithm with this false preference list, w will end up with a man m" that she truly prefers to both m and m'? (We can ask the same question for men, but will focus on the case of women for purposes of this question.)<p>
> Resolve this question by doing one of the following two things:<p>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(a) Give a proof that, for any set of preference lists, switching the order of a pair on the list cannot improve a woman's partner in the Gale- Shapley algorithm; or<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(b) Give an example of a set of preference lists for which there is a switch that 'Would improve the partner of a woman who switched preferences.

Considering the following case - where w3' is the altered preference list of w3.
|m1  | m2 | m3 | w1 | w2 | w3 | w3'|
|--- |--- |--- |--- |--- |--- |--- |
|w3  |w1  |w3  | m1 | m1 | m2 | m2 |
|w1  |w3  |w1  | m2 | m2 | m1 | m3 |
|w2  |w2  |w2  | m3 | m3 | m3 | m1 |

If we ran the G-S algorithm with the true preferences, then:<br>
- m1 would propose to w3, who would accept
- m2 would propose to w1, who would accept
- m3 would propose to w3, who would reject, as current partner m1 is ranked higher.
- m3 would then propose to w1, who would reject, as current partner m2 is ranked higher. 
- m3 would then propose to w2, who would accept. <p>

In this case, w3 is partnered with m1, her second choice. 

<p>

Now let's run it on altered preference list of w3:
- m1 would propose to w3', who would accept
- m2 would propose to w1, who would accept
- m3 would propose to w3', who would accept, as current partner m1 is ranked lower.
- m1 would now try to propse to w1, who would accept, as current partner m2 is ranked lower.
- m2 would now try to propose to w3', who would accept, as current partner m3 is ranked lower
- m3 would propose to w1, who rejects in favor of current partner
- m3 would propose to w2, who would accept.
<p>
In this case, w3 is partnered with m2, her first choice!
<p>

Therefore, it is **true**. By falsely switching the order of preferences, a woman may be able to get a more desirable partner. 