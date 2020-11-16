# k8s-mastodon
Kubenetes configuration to quickly deploy your mastodon instance.

## WARNING: still under testing
It's not a stable configuration and is not recommend to use in reality.

## How to deploy
### Requirements
- Kubenetes on your machines
- kubectl
- Python 3

### Step by Step
0. Setup your kubenetes clusters
1. Clone this repository and enter.
2. Change configurations (MUST DO, see next section).
3. `kubectl apply -k .`
4. Wait and look if the services run correctly.
4. Look at the ports of `mastodon-web` and `mastodon-streaming`, or deployment `mastodon`, setup port-forwarding and config your HTTP server to proxy. For example:
````
kubectl port-forward deployment/mastodon-mastodon 3000:3000
kubectl port-forward deployment/mastodon-mastodon 4000:4000
````

### Configuration
k8s-mastodon is not out of box, you must set variables to fit you needs.

0. In `kustomization.yaml`, change the database password.
1. Look at `mastodon/configuration.yaml` to change configurations for mastodon.
2. Save your VIPID private key and public key to files. Use `python mastodon/generate_secrets.py <path/to/private_key> <path/to/pubic_key> mastodon` in the root of the project to save secrets for mastodon. You may use `npm install web-push -g` to install web-push commandline tool and run `web-push generate-vapid-keys` to get them (NPM and NodeJS required).

3. (optional) Turn to `mastodon/system-pvsize.yaml` for avaliable spaces (default is 10GiB) to save user uploaded contents.
4. (optional) Turn to `smtp-gate/configuration.yaml` for email configuration if you prefer third-party server than own SMTP relay.
5. (optional) Turn to `postgresql/pvsize.yaml` for the avaliable space (default is 10GiB) of database.
