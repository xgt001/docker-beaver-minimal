import boto, boto.sqs

beaver_config_template = '''
[beaver]
logstash_version: 1
sqs_aws_region: ap-southeast-1
sqs_aws_queue: myqueue
sqs_aws_access_key:
sqs_aws_secret_key:
sincedb_path: /var/log/beaver/sincedb.sqlite

[/var/lib/docker/containers/**/*.log]
tags: Docker
'''

def get_queue():
  try:
    q_conn = boto.sqs.connect_to_region('ap-southeast-1')
    queues = q_conn.get_all_queues()
    print "Following are the active queues"
    for queue in queues:
	    print queue.name
    queue_to_use=raw_input('Please type the queue to be used:')
    beaver_config = beaver_config_template.replace('myqueue', queue_to_use)
    beaver_file = file('beaver.conf','w')
    beaver_file.write(beaver_config)
    beaver_file.close()
  except boto.exception.NoAuthHandlerFound:
  	print "Opsworks Role not mapped to SQS. Sorry."	

if __name__ == '__main__':
	get_queue()
