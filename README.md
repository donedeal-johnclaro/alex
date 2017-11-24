# alex
For Hackday on Nov 24, 2017

# Openshift

Upload the template.
```
oc process -f alex.yml -p GIT_BRANCH=master IMAGE_RELEASE_TAG=prd | oc create -f -
```

Deploy the app by setting the latest image to the image release tag
```
oc tag alex:latest alex:prd
```

Set the environment variables required for a service
```
oc env dc/alex-api $(cat prod.env)
```

Scale number of pods within a deployment
```
oc scale dc/alex-api --replicas=1
```

Delete
```
oc delete bc/alex
oc delete is/alex
oc delete dc/alex-api
oc delete routes/alex
oc delete svc/alex
```
