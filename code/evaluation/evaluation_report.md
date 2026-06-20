# Evaluation Report

## Final Strategy

* Gemini 2.5 Flash used for image analysis.
* Claim parser extracts claimed issue from conversation.
* User history used to generate risk flags.
* Decision engine combines image findings and risk context.
* Fallback mode returns safe values when model calls fail.

## Evaluation Dataset

* Evaluated on sample_claims.csv
* Generated final predictions for claims.csv

## Operational Analysis

### Model Calls

* Approximate sample claims calls: 20
* Approximate test claims calls: 44

### Images Processed

* Sample dataset images processed: ~20
* Test dataset images processed: 44+

### Cost

* Used Gemini free tier API.
* Estimated cost: $0

### Runtime

* Approximately 10-15 minutes due to rate limiting and batching.

### Rate Limit Handling

* Added delays between requests.
* Split processing into multiple batches.
* Used multiple API projects when quota limits were reached.

## Known Limitations

* supporting_image_ids currently defaults to "none".
* valid_image currently defaults to true.
* Fallback mode may return unknown values when model access fails.
