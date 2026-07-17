# Forms + Website Leads Integration
How every lead lands in the existing "Website Leads" Google Sheet.

## The two lead paths

### Path A: Forms (Medicare, Disability, General/Contact)
Use Tilda-native forms. In each form's settings:

1. **Fields** (visible): first_name, last_name, email, phone, state, product_interest, contact_method, message, consent (required checkbox)
2. **Hidden fields**: product_interest (preset on Medicare/Disability pages), source_page, referrer, utm_source, utm_medium, utm_campaign. The custom JS in main.js populates these automatically.
3. **Connect two receivers in Tilda's form settings:**
   - Email: Mischa@MrWrightInsures.com (instant notification)
   - Google Sheets: connect to the existing "Website Leads" sheet in the Website 2026 folder

**Column mapping** (Tilda asks you to map fields when connecting; use the sheet's existing headers):
| Sheet column | Form field |
|---|---|
| Timestamp | (automatic) |
| First name | first_name |
| Last name | last_name |
| Email | email |
| Phone | phone |
| State | state |
| Product interest | product_interest |
| Preferred contact | contact_method |
| Message | message |
| Source page | source_page |
| Referrer | referrer |
| UTM source/medium/campaign | utm_source / utm_medium / utm_campaign |
| Consent | consent |
| Lead source | set static value "Website" |

Leave appointment date/time, Calendly event type, lead status, assigned team, follow-up notes blank; those are for Path B and manual workflow.

**Success message** (only shown by Tilda after real submission): "Thank you. Your message has been received. We will contact you within one business day."

### Path B: Calendly bookings (LTC, Annuity, Life, General calls)
Calendly does not write to Google Sheets natively on all plans. Recommended, most reliable: **Zapier**.

1. Zap trigger: Calendly "Invitee Created"
2. Zap action: Google Sheets "Create Spreadsheet Row" -> Website Leads sheet
3. Map: invitee name -> First/Last, email -> Email, event start time -> Appointment date + Appointment time, event type name -> Calendly event type, set Lead source = "Website"
4. Repeat mapping per event type or use one Zap with the event-type field
5. UTM capture: Calendly passes utm parameters if present in the booking link; map utm_source/medium/campaign in the Zap

Alternative if avoiding Zapier cost: Google Apps Script webhook receiving Calendly's webhook (requires Calendly paid plan for webhooks) - happy to write this script when you're ready to wire it.

**Do not consider either path live until you've submitted a test through each form and booked a test Calendly slot, then seen both rows appear in the sheet.**

## Analytics events (GA4, when ready)
Add GA4 via Tilda's analytics settings, then these events are worth tracking: start_here_clicked, service_selected, calendly_clicked, lead_form_submitted, phone_clicked, email_clicked, review_link_clicked. Tilda supports click-event goals in its stats; GA4 custom events need small snippets - flag me when GA4 is set up and I'll write them.
