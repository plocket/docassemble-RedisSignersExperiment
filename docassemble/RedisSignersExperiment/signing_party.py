from docassemble.base.util import DARedis, DAObject

# Use and save data in redis if possible
class SigningParty(DAObject):
  # Only uses redis if url arguments exist to allow this module to be used independently of url arguments. Somewhere else will take care of authentication?
  def __init__(self, url_args):
    self.exists = False

    if 'action_id' in url_args:
      self.exists = True
      self.redis = DARedis()
      redis = self.redis

      # These intermediate vars are actually useful
      self.action_id = url_args[ 'action_id' ]
      self.id = url_args['party_id']
      self.action_data = redis.get_data( self.action_id )
      parties = self.action_data['parties']
      self.user = parties[ url_args['user_id'] ]  # For sms message
      party = parties[ self.id ]
      self.preview = self.action_data['preview']
      # Start as undefined when user first arrives?
      self.signature = valueOrNone( party, 'signature' )
      self.signature_date = valueOrNone( party, 'signature_date' )
      self.willing_to_sign = valueOrNone( party, 'willing_to_sign' )

  def amend(self, key, value):
    if self.exists:
      self.action_data['parties'][ self.id ][ key ] = value
      self.redis.set_data( self.action_id, self.action_data )

def valueOrNone( dictionary, key ):
  try: return dictionary[ key ]
  except: return None