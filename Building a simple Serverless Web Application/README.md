<h1>Overview</h1>

<p>This hand-on project is based on a practical project tutorial from AWS webpage. The idea of this project is to create a serverless web application that enables users to request unicorn rides from the Wild Rydes fleet. The application will present users with an HTML-based user interface for indicating a pick-up location and a RESTful web service on the backend to submit the request for dispatching a unicorn. The application will also provide facilities for users to register with the service and log in before requesting rides.</p>

<h1>Prerequisites</h1>

<p>To complete this project, we need to have an AWS CLI installed, an account with ArcGIS to add mapping to your app, a text editor, and a web browser. If you don't already have an AWS account, you can follow the Setting Up Your AWS Environment getting started guide for a quick overview.</p>

<h1>Application architecture overview</h1>

<p>The application architecture uses AWS Lambda, Amazon API Gateway, Amazon DynamoDB, Amazon Cognito, and AWS Amplify Console. Amplify Console provides continuous deployment and hosting of the static web resources including HTML, CSS, JavaScript, and image files which are loaded in the user's browser. JavaScript executed in the browser sends and receives data from a public backend API built using Lambda and API Gateway. Amazon Cognito provides user management and authentication functions to secure the backend API. Finally, DynamoDB provides a persistence layer where data can be stored by the API's Lambda function.</p>

<p><img alt="Image" title="icon" src="Serverless_WebApplication.png" /></p>

<strong>1. Static Web Hosting</strong>
<p>AWS Amplify hosts static web resources including HTML, CSS, JavaScript, and image files which are loaded in the user's browser.</p>

<strong>2. User Management</strong>
<p>Amazon Cognito provides user management and authentication functions to secure the backend API.</p>

<strong>3. Serverless Backend</strong>
<p>Amazon DynamoDB provides a persistence layer where data can be stored by the API's Lambda function.</p>

<strong>4. RESTful API</strong>
<p>JavaScript executed in the browser sends and receives data from a public backend API built using Lambda and API Gateway.</p>

<p>This personal project took about two hour to complete and all the aws resources I have used in this project are eligible for aws free-tier. Kindly check your aws Free-tier situation to ensure whether your aws account exceed the AWS Free Tier threshold.</p>