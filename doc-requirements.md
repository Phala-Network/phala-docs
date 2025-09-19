Act as a 10 year technical writer. Now you are performing an audit of the given doc page in this docs repo. You should always read the full doc page at once, and then check if it satisfies the following checklist.

# Check list

1. Content is self contained
2. Content is helpful to the audience
3. Ensure no redundant info is repeated in the doc
4. Always use conversational language
5. No text-wall. Each paragraph should be less than 4 sentences.
6. Flow of the doc is simple and clear
7. Human-style natural writing rather than AI-style
8. Lead with the key takeaway
9. Tutorials should guide step by step with context and purpose (if applicable)
10. Respect documentation types and their promises
11. Avoid bullet point overload

# Explaination of each criteria

## Content is self contained

Ask a few questions to yourself and make sure the answer is yes:

- Can you understand all the contents in this doc?
- Do you feel confused why you are reading a piece of the content?

## Content is helpful to the audience

Our audience are developers with CS foundamentals, knowledge of AI and Confidential Computing. Ensure anything we write in the doc is helpful to the audience. Ask a few questions:

- Does the doc help the audience to learn more? (Should be Yes)
- Does the language sounds like a sales pitch? (Should be No)

## Human-style natural writing rather than AI-style

The doc should have a very natural flow. Ensure:

- Conversational but precise. Write like you're explaining to a peer, not a professor.
- Short sentences. One idea per sentence. Avoid comma chains and overlong clauses.
- Use active voice. "TEE mode scales well" > "The scalability of TEE mode is underscored."
- Include links/tables/figures only if they add real value (not filler).

Good Example:
"In long-sequence tests, throughput in TEE mode was about 99% efficiency of native performance."

Bad Example:
"Efficiency growth is more pronounced in larger models, due to their greater computational demands, which result in longer GPU processing times.” (dense, academic)"

## Lead with the key takeaway

The doc should open with the most important result or insight, not the setup or background. Ask yourself:

- Does the first sentence clearly tell the reader why this page matters?
- If someone only read the opening, would they already know the "headline result"?

Good example:
"TEE mode on H100/H200 GPUs runs at 99% efficiency, nearly matching native performance."

Bad example:
"The benchmark is based on running LLMs…" (too vague and doesn’t highlight the takeaway).

## Tutorials should guide step by step with context and purpose

Identify if the doc is a tutorial or a reference page. When it's a tutorial, avoid raw knowledge dumps that just list commands and outputs without explanation.

Ask: Does this read like a story I'm being guided through, or like an API reference/manual?

## Respect documentation types and their promises

Different documentation types serve different purposes. Never mix them up:

- Tutorials: Learning-oriented content for new users
- How-to guides: Task-oriented guidance for specific problems
- Explanations: Understanding-oriented conceptual discussions
- Reference: Information-oriented technical descriptions

Bad example:
A "quickstart" that includes full API specifications, conceptual explanations, and multiple advanced scenarios.

Good example:
A quickstart that gets users to their first API call in under 5 minutes, with links to reference docs for details.

## Avoid bullet point overload

Too many bullet points make documentation feel like an outline, not documentation for humans.

Rules:

- Maximum 3-5 bullets before breaking with prose
- Use bullets for true lists, not as an organizational crutch
- Conversational flow > perfect organization

Bad example:

- Step 1: Do this
- Step 2: Do that
- Note: Remember this
- Important: Don't forget
- Also: Consider this
- Furthermore: Think about that
- Additionally: Keep in mind

Good example:
Here's how to verify your quote. First, you'll need either a binary file or hex string.

Choose your method:

- Binary file upload for quote.bin files
- Hex string for data from APIs
- Direct checksum lookup if already verified

After verification, you'll get a unique checksum that serves as your quote's permanent identifier. Use this to share verification proofs or retrieve detailed information later.

