# Deploy and Manage CVMs

## Choose Your Preferred Method

Phala Cloud offers multiple ways to create and deploy your Confidential Virtual Machine (CVM), accommodating different workflows and preferences.

### Option 1: Using the Phala Cloud UI (Recommended for Beginners)

If you prefer a visual interface with guided steps, the Phala Cloud UI provides an intuitive experience for creating your CVM:

[**Create with Docker Compose →**](create-with-docker-compose.md)

The Phala Cloud UI is ideal for:

* First-time users of Phala Cloud
* Visual learners who prefer graphical interfaces
* Quick deployments without command-line knowledge

### Option 2: Using the Command Line Interface (CLI)

For developers who prefer terminal-based workflows or need to automate deployments:

[**Follow the CLI Guide →**](../advanced-deployment-options/start-from-cloud-cli.md)

The CLI approach is perfect for:

* Experienced developers
* DevOps automation
* CI/CD pipeline integration
* Script-based deployments

## CVM Management Features

Phala Cloud provides a comprehensive management system for your CVMs, allowing you to monitor, upgrade, and resize your applications.

### Monitoring

* **CVM Status**: Track the health and status of your CVMs
* **Resource Usage**: Monitor CPU, memory, and storage consumption
* **Logs**: View application logs and system messages

### Upgrades

* **Environment Variables**: Update your application's environment variables
* **Docker Images**: Upgrade your application's Docker image
* **Resource Allocation**: Adjust your CVM's CPU, memory, and storage

### Resizing

* **Resource Scaling**: Dynamically adjust your CVM's CPU, memory, and storage
* **Cost Optimization**: Reduce your cloud spending by downsizing your CVM

### Security

* **Data Protection**: E2E encrypt your sensitive data at rest
* **Access Control**: Restrict access to your CVMs and logs

## CVM Management API

Phala Cloud provides a [API](https://cloud-api.phala.network/docs) for managing your CVMs, allowing you to automate your CVM management tasks.

## Next Steps

After creating your CVM, you'll want to:

* [Access to your applications](../building-with-tee/access-your-applications.md)
* [Set up monitoring](debugging-and-analyzing-logs/check-logs.md)
