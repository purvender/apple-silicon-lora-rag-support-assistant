# Example four-mode evaluation (excerpt)

Sample output from `python scripts/eval_compare.py` (Q1 only). Full reports are generated locally.

## Q1

**Question:** I forgot my password and the reset email never arrived.

### base_only

**Retrieved sources:** None

**Answer:**

I'm so sorry to hear that you're having trouble with your account.
…

### tuned_only

**Retrieved sources:** None

**Answer:**

First, check your spam and promotions folders for an email from AcornDesk…

### base_rag

**Retrieved sources:** [{"source": "passwords.txt"}]

**Answer:**

You can reset your password using the "Forgot Password" link on the sign-in page…

### tuned_rag

**Retrieved sources:** [{"source": "passwords.txt"}]

**Answer:**

First, check your spam and promotions folders. If there is no response, reply with your workspace name…
