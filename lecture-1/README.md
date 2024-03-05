# Harvard CS50 AI - Lecture 1 - Knowledge

<details>
<summary>Terminology</summary>

- **Sentence** is an assertion about the world in a knowledge representation language. A sentence is how AI stores knowledge and uses it to infer new information.
- **Propositions** are statements about the world that can be _either_ true or false.
- **Model** is an assignment of a truth value to every proposition.
- **Knowledge base (KB)** is a set of sentences known by a knowledge-based agent. This is knowledge that the AI is provided about the world in the form of propositional logic sentences that can be used to make additional inferences about the world.
- **Entailment (⊨)** If `α ⊨ β` (α entails β), then in any world where `α` is true, `β` is true, too. _For example, if `α`: “It is a Tuesday in January” and `β`: “It is January,” then we know that `α ⊨ β`. If it is true that it is a Tuesday in January, we also know that it is January. Entailment is different from implication. Implication is a logical connective between two propositions. Entailment, on the other hand, is a relation that means that if all the information in `α` is true, then all the information in `β` is true._

</details>

<details>
<summary>Propositional Logic</summary>

- **Not (¬)** inverses the truth value of the proposition. So, for example, if `P`: “It is raining,” then `¬P`: “It is not raining”.
- **And (∧)** connects two different propositions. When these two proposition, `P` and `Q`, are connected by `∧`, the resulting proposition `P ∧ Q` is true only in the case that both `P` and `Q` are true.
- **Or (∨)** is true as as long as either of its arguments is true. This means that for `P ∨ Q` to be true, at least one of `P` or `Q` has to be true.
- **Implication (→)** represents a structure of “if `P` then `Q`.” For example, if `P`: “It is raining” and `Q`: “I’m indoors”, then `P → Q` means “If it is raining, then I’m indoors.” In the case of `P` implies `Q` (`P → Q`), `P` is called the **antecedent** and `Q` is called the **consequent**.
- **Biconditional (↔)** is an implication that goes both directions. You can read it as “if and only if.” `P ↔ Q` is the same as `P → Q` and `Q → P` taken together. For example, if `P`: “It is raining.” and `Q`: “I’m indoors,” then `P ↔ Q` means that “If it is raining, then I’m indoors,” and “if I’m indoors, then it is raining.” This means that we can infer more than we could with a simple implication. If `P` is false, then `Q` is also false; if it is not raining, we know that I’m also not indoors.

</details>

<details>
<summary>Inference (Rules)</summary>

</details>

<details>
<summary>First Order Logic</summary>

**Universal Quantification**
Quantification is a tool that can be used in first order logic to represent sentences without using a specific constant symbol. Universal quantification uses the symbol `∀` to express “for all.” So, for example, the sentence `∀x. BelongsTo(x, Gryffindor) → ¬BelongsTo(x, Hufflepuff)` expresses the idea that it is true for every symbol that if this symbol belongs to Gryffindor, it does not belong to Hufflepuff.

**Existential Quantification**
Existential quantification is an idea parallel to universal quantification. However, while universal quantification was used to create sentences that are true for all `x`, existential quantification is used to create sentences that are true for at least one `x`. It is expressed using the symbol `∃`. For example, the sentence `∃x. House(x) ∧ BelongsTo(Minerva, x)` means that there is at least one symbol that is both a house and that Minerva belongs to it. In other words, this expresses the idea that Minerva belongs to a house.

Existential and universal quantification can be used in the same sentence. For example, the sentence `∀x. Person(x) → (∃y. House(y) ∧ BelongsTo(x, y))` expresses the idea that if `x` is a person, then there is at least one house, `y`, to which this person belongs. In other words, this sentence means that every person belongs to a house.

</details>
