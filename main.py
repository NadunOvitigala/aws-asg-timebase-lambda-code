import boto3

def lambda_handler(event, context):
    

    autoscaling = boto3.client('autoscaling')
    
    auto_scaling_group_name = event['AutoScalingGroupName']
    
    desired_capacity = autoscaling.describe_auto_scaling_groups(AutoScalingGroupNames=[auto_scaling_group_name])['AutoScalingGroups'][0]['DesiredCapacity']
    
    desired_capacity = event['DesiredCapacity']
    
    autoscaling.set_desired_capacity(AutoScalingGroupName=auto_scaling_group_name, DesiredCapacity=desired_capacity)
    
    return {
        'statusCode': 200
    }