# Activity

In order to give the user insight in what is going on in her personal finance Tink runs many calculations every time data is processed and tries to find the most interesting fact from your personal finance. This information in presented via an Activity. Different result could be returned from different times activities are listed. This since the Tink engine may have detected something of more interest than before and leaves out what before was present. The key property on the activity is persistent between queries if the activity is based on the same data. Hence if an activity with a new key is return it means this is a new unseen activity.

Each activity has a data object serialized in its content property. This can be deserialized based on the type of activity.
