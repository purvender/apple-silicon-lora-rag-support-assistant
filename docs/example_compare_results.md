# Four-mode evaluation

Questions from `data/eval/test_prompts.txt` across base only, tuned only, base + RAG, tuned + RAG.

## Q1

**Question:** I forgot my password and the reset email never arrived.

### base_only

**Retrieved sources:** None

**Answer:**

I'm so sorry to hear that you're having trouble with your account.

To reset your password, please:

1. Go to the login page and click on "Forgot Password?"
2. Enter your email address and click "Submit"
3. You will receive an email with a link to reset your password

If you're still having trouble, please contact our support team and we'll be happy to assist you.

### tuned_only

**Retrieved sources:** None

**Answer:**

First, check your spam and promotions folders for an email from AcornDesk. If there is nothing there after 5 minutes, confirm you have entered the correct login email and then wait 15 minutes before checking again.

### base_rag

**Retrieved sources:** [{"source": "passwords.txt"}]

**Answer:**

You can reset your password using the "Forgot Password" link on the sign-in page. If you don't receive the reset email within 5-10 minutes, check your spam and promotions folders.

### tuned_rag

**Retrieved sources:** [{"source": "passwords.txt"}]

**Answer:**

First, check your spam and promotions folders. If there is no response, reply with your workspace name, account email, and the original login email. Our team will manually reset your password.

## Q2

**Question:** Can you extend my AcornDesk trial by one week?

### base_only

**Retrieved sources:** None

**Answer:**

"Hello, I'd be happy to help you with your AcornDesk trial. I can extend your trial by one week. Would you like me to do that for you?"

### tuned_only

**Retrieved sources:** None

**Answer:**

Yes. Extend your trial by sending us an email with your workspace name, team size, and the reason for the extension. We will apply the one-week extension if possible.

### base_rag

**Retrieved sources:** [{"source": "trial_extensions.txt"}]

**Answer:**

Yes, you can extend your AcornDesk trial by one week.

### tuned_rag

**Retrieved sources:** [{"source": "trial_extensions.txt"}]

**Answer:**

Yes. Extend your trial by 7 days. Reply with your workspace name, teammates invited, and the reason for the extension.

## Q3

**Question:** Can I get a refund on my annual plan if we decide not to use AcornDesk?

### base_only

**Retrieved sources:** None

**Answer:**

If we decide not to use AcornDesk, you can cancel your annual plan and request a full refund. Please note that you will not be charged for the unused portion of your plan.

### tuned_only

**Retrieved sources:** None

**Answer:**

Yes. If you decide not to use AcornDesk after purchasing an annual plan, contact support within 14 days with your workspace name and billing email. We will review your case and apply a prorated refund for the unused portion of the year.

### base_rag

**Retrieved sources:** [{"source": "refunds.txt"}]

**Answer:**

You can request a refund for your annual plan within 14 days of purchase. However, since you're considering canceling your AcornDesk subscription, you'll need to contact support to initiate the refund process.

### tuned_rag

**Retrieved sources:** [{"source": "refunds.txt"}]

**Answer:**

Yes. If you decide not to use AcornDesk after purchasing an annual plan, contact support with your account email and order ID. We will review your case and apply a partial refund if you decide to cancel.

## Q4

**Question:** How do I download past invoices for my finance team?

### base_only

**Retrieved sources:** None

**Answer:**

To download past invoices for your finance team, follow these steps:

1. Log in to your company's online portal or system.
2. Navigate to the 'Invoices' or 'Financials' section.
3. Look for the 'Download Invoices' or 'Export Invoices' option.
4. Select the specific period (e.g., month, quarter, year) and the 'File Type' (e.g., PDF, Excel).
5. Choose the 'Finance Team' or 'Authorized User' option to ensure only authorized personnel can access the files.

Please note that you may need to log in as an authorized user or have a specific role to access the download feature.

### tuned_only

**Retrieved sources:** None

**Answer:**

To download past invoices, go to Settings → Billing and click “Download invoices.” Each invoice can be viewed in a spreadsheet format for your finance team.

### base_rag

**Retrieved sources:** [{"source": "billing.txt"}]

**Answer:**

You can download past invoices from Settings → Billing → Invoices.

### tuned_rag

**Retrieved sources:** [{"source": "billing.txt"}]

**Answer:**

Past invoices can be downloaded from Settings → Billing → Invoices. Each invoice can be viewed in the browser or downloaded as a PDF.

## Q5

**Question:** Where can I change the billing contact email address?

### base_only

**Retrieved sources:** None

**Answer:**

You can change your billing contact email address by contacting our billing department directly. They will be able to assist you with the necessary steps to update your email address.

### tuned_only

**Retrieved sources:** None

**Answer:**

To change the billing contact email, go to Settings → Billing and update the Billing contact email field. Future invoices and billing notifications will be sent to the new address.

### base_rag

**Retrieved sources:** [{"source": "billing.txt"}]

**Answer:**

You can change the billing contact email address under Settings → Billing → Billing contact email.

### tuned_rag

**Retrieved sources:** [{"source": "billing.txt"}]

**Answer:**

Billing contact email can be updated under Settings → Billing → Billing contact email. Future invoices and billing notifications will use the new address.

## Q6

**Question:** How do I invite a new teammate and control their permissions?

### base_only

**Retrieved sources:** None

**Answer:**

To invite a new teammate and control their permissions, follow these steps:

1. Log in to your account.
2. Click on "Invite Team Members" in the top navigation bar.
3. Enter the teammate's email address and select the team they belong to.
4. Choose the permissions you want to assign to the teammate (e.g., read-only, edit, or full access).
5. Review and confirm the invitation.

Once invited, you can manage their permissions by:

* Editing permissions: Click on the teammate's name and edit their permissions.
* Removing permissions: Click on the teammate's name and select "Remove" from the permissions menu.

Note: You can also use the "Invite Team Members" feature in your organization's system, if available.

### tuned_only

**Retrieved sources:** None

**Answer:**

To invite a teammate, go to Settings → Team and click “Invite teammate.” Enter their email address, choose a role, and send the invite. They will receive an email with a link to join your workspace.

### base_rag

**Retrieved sources:** [{"source": "team_permissions.txt"}]

**Answer:**

To invite a new teammate and control their permissions:

1. Invite teammate: Go to Settings → Team → Invite teammate.
2. Enter their email: Enter the email address of the new teammate.
3. Choose a role: Select the role (Agent, Admin, or Viewer) for the new teammate.
4. Send the invite: Send the invite to the new teammate.

Note: Only Admins can access billing settings.

### tuned_rag

**Retrieved sources:** [{"source": "team_permissions.txt"}]

**Answer:**

To invite a teammate, go to Settings → Team → Invite teammate, enter their email, choose a role, and send the invite. The teammate will receive an email with a link to join your workspace.

## Q7

**Question:** I want to cancel but keep access until the end of this billing period.

### base_only

**Retrieved sources:** None

**Answer:**

"I understand your request. To cancel your subscription while keeping access until the end of the billing period, you can try the following options:

1. Contact our billing department to cancel your subscription.
2. Check your email for any cancellation instructions.
3. Visit our website and log in to your account to cancel your subscription.

Please note that we may not be able to cancel your subscription if you've already paid for the billing period. If you need help with the cancellation process, please contact our billing department for assistance."

### tuned_only

**Retrieved sources:** None

**Answer:**

To cancel and keep access until the end of the current billing period, go to Settings → Billing and change the plan to the one that matches your use case. Your access will remain valid until the end of the current billing period.

### base_rag

**Retrieved sources:** [{"source": "cancellation.txt"}]

**Answer:**

You can cancel your plan and keep access until the end of the current billing period.

### tuned_rag

**Retrieved sources:** [{"source": "cancellation.txt"}]

**Answer:**

[ERROR]
/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Traceback (most recent call last):
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/urllib3/connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/urllib3/connectionpool.py", line 1093, in _validate_conn
    conn.connect()
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/urllib3/connection.py", line 796, in connect
    sock_and_verified = _ssl_wrap_socket_and_match_hostname(
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/urllib3/connection.py", line 975, in _ssl_wrap_socket_and_match_hostname
    ssl_sock = ssl_wrap_socket(
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/urllib3/util/ssl_.py", line 483, in ssl_wrap_socket
    ssl_sock = _ssl_wrap_socket_impl(sock, context, tls_in_tls, server_hostname)
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/urllib3/util/ssl_.py", line 527, in _ssl_wrap_socket_impl
    return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/ssl.py", line 500, in wrap_socket
    return self.sslsocket_class._create(
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/ssl.py", line 1040, in _create
    self.do_handshake()
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/ssl.py", line 1309, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLEOFError: EOF occurred in violation of protocol (_ssl.c:1129)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/urllib3/connectionpool.py", line 787, in urlopen
    response = self._make_request(
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/urllib3/connectionpool.py", line 488, in _make_request
    raise new_e
urllib3.exceptions.SSLError: EOF occurred in violation of protocol (_ssl.c:1129)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/requests/adapters.py", line 644, in send
    resp = conn.urlopen(
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/urllib3/connectionpool.py", line 841, in urlopen
    retries = retries.increment(
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/urllib3/util/retry.py", line 535, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /api/models/mlx-community/Llama-3.2-1B-Instruct-4bit/revision/main (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)')))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/mlx_lm/__main__.py", line 30, in <module>
    submodule.main()
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/mlx_lm/generate.py", line 1293, in main
    model, tokenizer = load(
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/mlx_lm/utils.py", line 320, in load
    model_path = _download(path_or_hf_repo, revision=revision)
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/mlx_lm/utils.py", line 133, in _download
    snapshot_download(
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/huggingface_hub/utils/_validators.py", line 114, in _inner_fn
    return fn(*args, **kwargs)
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/huggingface_hub/_snapshot_download.py", line 165, in snapshot_download
    repo_info = api.repo_info(repo_id=repo_id, repo_type=repo_type, revision=revision)
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/huggingface_hub/utils/_validators.py", line 114, in _inner_fn
    return fn(*args, **kwargs)
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/huggingface_hub/hf_api.py", line 2867, in repo_info
    return method(
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/huggingface_hub/utils/_validators.py", line 114, in _inner_fn
    return fn(*args, **kwargs)
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/huggingface_hub/hf_api.py", line 2660, in model_info
    r = get_session().get(path, headers=headers, timeout=timeout, params=params)
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/requests/sessions.py", line 602, in get
    return self.request("GET", url, **kwargs)
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/requests/sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/requests/sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/huggingface_hub/utils/_http.py", line 96, in send
    return super().send(request, *args, **kwargs)
  File "/Users/purvenderhooda/llm-lab-m1/.venv/lib/python3.9/site-packages/requests/adapters.py", line 675, in send
    raise SSLError(e, request=request)
requests.exceptions.SSLError: (MaxRetryError("HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /api/models/mlx-community/Llama-3.2-1B-Instruct-4bit/revision/main (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)')))"), '(Request ID: 4c50813f-cdca-45f3-af82-135ae713701f)')

## Q8

**Question:** Can I switch from monthly to annual billing?

### base_only

**Retrieved sources:** None

**Answer:**

Yes, you can switch from monthly to annual billing. However, you'll need to contact our billing department to initiate the process. They'll guide you through the necessary steps to make the switch.

### tuned_only

**Retrieved sources:** None

**Answer:**

Yes. Contact support with your workspace name and billing email so we can adjust your plan at renewal.

### base_rag

**Retrieved sources:** [{"source": "billing.txt"}]

**Answer:**

You can switch from monthly to annual billing under Settings → Billing by selecting an annual plan at the next renewal.

### tuned_rag

**Retrieved sources:** [{"source": "billing.txt"}]

**Answer:**

Yes. To switch from monthly to annual billing, go to Settings → Billing and select the annual plan. The downgrade will occur at the next renewal, and you will be charged for the next year.

## Q9

**Question:** What happens to my data after I cancel my subscription?

### base_only

**Retrieved sources:** None

**Answer:**

After you cancel your subscription, your data will be removed from our system. However, we will still retain your account information and any necessary billing details for a short period (usually 30 days) to facilitate the cancellation process.

### tuned_only

**Retrieved sources:** None

**Answer:**

Your data will remain on our servers until the end of the current billing period. After cancellation, we will delete all data from our systems. If you have work ongoing that requires access, share your workspace name and billing email, and we will grant access for the remainder of the billing period.

### base_rag

**Retrieved sources:** [{"source": "cancellation.txt"}]

**Answer:**

After you cancel your subscription, your workspace data will be deleted from AcornDesk systems within 30 days.

### tuned_rag

**Retrieved sources:** [{"source": "cancellation.txt"}]

**Answer:**

After cancellation, workspace data is deleted from AcornDesk systems within 30 days of cancellation. You can export data from Settings → Data export before cancellation.

## Q10

**Question:** How do I contact AcornDesk support if none of this solves my problem?

### base_only

**Retrieved sources:** None

**Answer:**

If you're not getting the help you need, you can contact AcornDesk support through our website's contact form. You can also call us at 1-800-ACORD (1-800-232-6733) or email us at [support@acorndesk.com](mailto:support@acorndesk.com).

### tuned_only

**Retrieved sources:** None

**Answer:**

You can contact support via email (support@acorndesk.com), chat on the website, or call us during business hours (Monday–Friday, 9 AM – 5 PM EST).

### base_rag

**Retrieved sources:** [{"source": "billing.txt"}]

**Answer:**

You can contact AcornDesk support through the following methods:

1. Email: You can reply to this FAQ or contact us directly via email at [support@acorndesk.com](mailto:support@acorndesk.com).
2. Live Chat: You can also initiate a live chat with our support team at [acorndesk.com/support](http://acorndesk.com/support).
3. Phone: You can call us at +1 (123) 456-7890 (US-based) or +44 (111) 222-3333 (UK-based).

Please note that our support team is available to assist you 24/7, but we may not be able to respond immediately due to high volume of inquiries.

### tuned_rag

**Retrieved sources:** [{"source": "billing.txt"}]

**Answer:**

You can contact support via email at support@acorndesk.com or use the ticket system in Settings → Billing → Tickets. Our team is available Monday–Friday, 9:00 AM – 5:00 PM EST.
