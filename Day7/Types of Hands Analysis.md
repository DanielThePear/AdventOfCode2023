Identifying the hand type
---
**Five of a Kind**: `len(set(hand)) == 1`

**Four of a Kind**: `len(set(hand)) == 2`  
**Full House**: `len(set(hand)) == 2`  
A **Full House** will always have 3 of the same card, so if we check the amount of each card in the hand, and the most common one appears 3 times, then we have a **Full House**. Otherwise, we have a **Four of a Kind**.

**Three of a Kind**: `len(set(hand)) == 3`    
**Two Pair**: `len(set(hand)) == 3`  
A **Three of a Kind** will always have 3 of the same card, so if we check the amount of each card in the hand, and the most common one appears 3 times, then we have a **Three of a Kind**. Otherwise, we have a **Two Pair**.

**One Pair**: `len(set(hand)) == 4`  
**High Card**: `len(set(hand)) == 5`


Replacing `J`
---

**High Card**: `2345J` (1 instance of `J`)  
Promote to **One Pair** by replacing `J` with most common, which is NOT `J` (i.e. `2`): `23452`

**One Pair**: `A2JA4` (1 instance of `J`)  
Promote to **Three of a Kind** by replacing `J` with the most common (i.e. `A`): `A2AA4`  
**One Pair**: `J23J4` (2 instances of `J`)  
Promote to **Three of a Kind** by replacing `J` with any (or most common) (i.e. `2`): `22324`

**Two Pair**: `23J32` (1 instance of `J`)  
Promote to **Full House** by replacing `J` with either of the most common (i.e. `3`): `23332`  
**Two Pair**: `J343J` (2 instances of `J`)  
Promote to **Four of a Kind** by replacing `J` with the most common (i.e. `3`): `33433`

**Three of a Kind**: `TTT9J` (1 instance of `J`)  
Promote to **Four of a Kind** by replacing `J` with the most common (i.e. `T`): `TTT9T`  
**Three of a Kind**: `JJJ98` (3 instances of `J`)  
Promote to **Four of a Kind** by replacing `J` with either singular value (i.e. `9`): `99998`

**Full House**: `J333J` (2 instances of `J`)  
Promote to **Five of a Kind** by replacing `J` with most common (i.e. `3`): `33333`  
**Full House**: `2JJJ2` (3 instances of `J`)  
Promote to **Five of a Kind** by replacing `J` with least common (i.e. `2`): `22222`

**Four of a Kind**: `AAJAA` (1 instance of `J`)  
Promote to **Five of a Kind** by replacing `J` with most common (i.e. `A`): `AAAAA`  
**Four of a Kind**: `JJ8JJ` (4 instances of `J`)  
Promote to **Five of a Kind** by replacing `J` with least common (i.e. `8`): `88888`

**Five of a Kind**: `JJJJJ` (5 instances of `J`)  
Replace `J` with `A` (highest value): `AAAAA`

Now that we have an exhaustive analysis of the possible hands with `J`, we can create a function that will replace `J` with the appropriate value. Below are the similarities between how many instances of `J` there are and what we should replace it with. We don't actually care what hand we have, only how many instances of `J` there are.

**One instance of `J`**: Replace `J` with most common which is NOT `J`  
**Two instances of `J`**: Replace `J` with most common  
**Three instances of `J`**: Replace `J` with the least common  
**Four instances of `J`**: Replace `J` with the least common  
**Five instances of `J`**: Replace `J` with `A`