# Versioning

The Tink API is versioned using a version identifier in the endpoint URI. The current version of the API is v1 and we expect this to be the case for the forseable future. New properties and data models are continuously added to the v1 API, but it will remain backwards compatible with this specification until deprecated.

Please note that obsolete fields that are not listed in this documentation can be present on some of the responses received from the Tink API. These obsolete fields are artifacts of pre-production data models and any 3rd-party API consumer should account for the fact that unknown properties can be present.
