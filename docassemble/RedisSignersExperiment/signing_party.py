from docassemble.base.util import DARedis, Individual, log #, DAObject

# Use and save data in redis if possible
#class SigningParty(DAObject):
class SigningParty():
  # Only uses redis if url arguments exist to allow this module to be used independently of url arguments. Somewhere else will take care of authentication?
  def __init__(self, url_args, obj):
    self.exists = False
    log( 'a', 'console' )
    # In url_args there should be:
    # action_key, user_id, party_id

    if 'action_key' in url_args:
      log( 'b', 'console' )
      self.exists = True
      self.redis = DARedis()
      redis = self.redis

      # These intermediate vars are actually useful
      self.action_key = url_args[ 'action_key' ]
      self.id = url_args['party_id']
      self.action_data = redis.get_data( self.action_key )
      parties = self.action_data['parties']
      self.user = parties[ url_args['user_id'] ]  # For sms message
      party = parties[ self.id ]
      #self.preview = self.action_data['preview']
      #self.preview = self.action_data['sign_doc']

      # Start as undefined when user first arrives?
      self.signature = valueOrNone( party, 'signature' )
      self.signature_date = valueOrNone( party, 'signature_date' )
      self.willing_to_sign = valueOrNone( party, 'willing_to_sign' )
      self.has_signed = valueOrNone( party, 'has_signed' )

      #log( 'willing_to_sign', 'console' )
      #log( valueOrNone( party, 'willing_to_sign' ), 'console' )
      #self.amend( 'willing_to_sign', valueOrNone( party, 'willing_to_sign' ))
      #log( self.willing_to_sign, 'console' )
    else:
      return False

  def amend(self, key, value):
    if self.exists:
      log( 'module:', 'console' )
      log( self.action_data['parties'][ self.id ], 'console' )
      log( key, 'console' )
      log( value, 'console' )
      setattr( self.action_data['parties'][ self.id ], key, value ) #.setAttribute( key, value )
      self.redis.set_data( self.action_key, self.action_data )

def valueOrNone( dictionary, key ):
  try:
    log( 'valueOrNone', 'console' )
    log( repr(dictionary), 'console' )
    return dictionary[ key ]
  except: return None


redis = DARedis()
  
def amend_signer( url_args, key, value ):
  if 'action_key' in url_args:
    party_id = url_args['party_id']
    action_data = redis.get_data( url_args['action_key'] )

    # set party key
    action_data['parties'][ party_id ][ key ] = value
    redis.set_data( url_args[ 'action_key' ], action_data )
    return action_data['parties'][ party_id ]
  else:
    return None
  
def get_signer( url_args ):
  if 'action_key' in url_args:
    party_id = url_args['party_id']
    if party_id in redis.get_data( url_args['action_key'] )['parties']:
      return redis.get_data( url_args['action_key'] )['parties'][ party_id ]
    else:
      return False
  else:
    return False
