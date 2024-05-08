<h1>Overview</h1>
<p>AWS Amplify will be used to host the static web resources for this web application with continuous deployment built in. There is also another option to host the static web hosting by using web hosting function in AWS S3. 
    However, in this project, I would deploy the AWS Amplify for hosting the static web hosting. With the Amplify Console, you can easily deploy and host full-stack web apps using a git-based workflow. 
    After that, we will add dynamic functionality to these pages using JavaScript to call RESTful APIs builts with AWS Lambda and AWS API Gateway.</p>

<h1>Architect Overview</h1>
<p>All of my static web content including HTML, CSS, JavaScript, images, and other files will be managed by AWS Amplify Console. Users access the website through public URL exposed by AWS Amplify Console.
    There is no need to run any servers as AWS Amplify works together with Lambda and API Gateway as a whole serverless architect, providing a scalable, reliable, low latency and cost-effective solution for hosting a web application.
</p>

<h1>Let's start with:</h1>

<h2>Select a region</h2>

<p>There is a list of regions to choose from to pick up a region for the web application. Following the instruction from AWS, chosing a region usually is based on location of majority of customers, compliances, pricing of the services, and availability of services. In this case, I would choose EU Frankfurt as the region of my web application.</p>

<h2>Create a git repository</h2>

<p>There are two options to manage the source code for this project. However, I choose to use Github instead of AWS CodeCommit.
    First, AWS CLI need to be installed into local machine if it is not installed in advanced as we are going to work from AWS CLI for this section.
    Create a repository and start to clone the ready code from AWS S3.  

</p>

<h2>Populate the git repository</h2>

<p>Copy the code content of the static web page from S3 and clone it into the local repository.</p>

<h2>Enable web hosting with the AWS Amplify Console</h2>

<p>Next use the AWS Amplify Console to deploy the website you've just committed to git. The Amplify Console takes care of the work of setting up a place to store your static web application code and provides a number of helpful capabilities to simplify both the lifecycle of that application as well as enable best practices.</p>

<h2>Modify the site</h2>

<p>The following code block is an example in the terminal window:
    <code>$ git add index.html 
$ git commit -m "updated title"
[master dfec2e5] updated title
 1 file changed, 1 insertion(+), 1 deletion(-)

$ git push
Counting objects: 3, done.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 315 bytes | 315.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: processing 
To https://git-codecommit.us-east-1.amazonaws.com/v1/repos/wildrydes-site
   2e9f540..dfec2e5  master -> master</code>
    </p>

<h2></h2>

<p></p>

<p></p>
