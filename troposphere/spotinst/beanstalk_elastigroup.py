from troposphere.cloudformation import AWSCustomObject, AWSProperty, integer

class BeanstalkElastigroupLaunchSpecification(AWSProperty):
    props = {
        'monitoring': (boolean, False),
        'imageId': (basestring, False),
        'keyPair': (basestring, True),
        'securityGroupIds': ([basestring], True)
    }


class BeanstalkElastigroupCapacity(AWSProperty):
    props = {
        'minimum': (integer, False),
        'maximum': (integer, False),
        'target': (integer, True),
    }


class BeanstalkEnvironmentNameConfig(AWSProperty):
    props = {
        'Ref': (basestring, True)
    }


class BeanstalkEnvironmentConfig(AWSProperty):
    props = {
        'environmentName': (BeanstalkEnvironmentNameConfig, True)
    }

# class BeanstalkElastigroupStrategy(AWSProperty):
#     props = {
#         'risk': (integer, False),
#         'maximum': (basestring, False),
#     }

class BeanstalkElastigroupConfig(AWSProperty):
    props = {
        'name': (basestring, True)
        'region': (basestring, True),
        'product': (basestring, True),
        # 'strategy': (BeanstalkElastigroupStrategy, True),
        'capacity': (BeanstalkElastigroupCapacity, True),
        'launchSpecification': (BeanstalkElastigroupLaunchSpecification, False),
        'spotInstanceTypes': ([basestring], True),
        'beanstalk': (BeanstalkEnvironmentConfig, True)
    }


class BeanstalkElastigroup(AWSCustomObject):
    resource_type = "Custom::beanstalkElastigroup"

    props = {
        'ServiceToken': (basestring, True),
        'accessToken': (basestring, True),
        'accountId': (basestring, True),
        'beanstalkElastigroup': (BeanstalkElastigroupConfig, True)
}
