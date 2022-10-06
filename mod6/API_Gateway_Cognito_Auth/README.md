## Amazon Cognito
### AWS CLI���g�p����Cognito���[�U�[�v�[���ւ̃T�C���C���̗�

1. �K�v�ȏ������ϐ��ɐݒ�

```
USER_POOL_ID=(Congnito���[�U�[�v�[����ID)
CLIENT_ID=(Congnito���[�U�[�v�[����Application Client ID)
USER_EMAIL=(���[�U�[�̃��[���A�h���X)
PASSWORD=(���[�U�[�̃p�X���[�h)
```

2. AWS CLI�R�}���h�ŃT�C���C��

```
 aws cognito-idp admin-initiate-auth \
  --user-pool-id ${USER_POOL_ID} \
  --client-id ${CLIENT_ID} \
  --auth-flow ADMIN_NO_SRP_AUTH \
  --auth-parameters "USERNAME=${USER_EMAIL},PASSWORD=${PASSWORD}"
```

3. API Gateway��JWT�܂���Cognito�I�[�T���C�U�[���ݒ肳�ꂽAPI�ɃA�N�Z�X����ꍇ�A�Ԃ��ꂽJWT�g�[�N������ID�g�[�N���̒l�� Authorization�w�b�_�ɐݒ肵�ă��N�G�X�g�𔭍s����

```
curl (API Gateway URL) -H "Authorization:(ID�g�[�N��)"
```


### AWS CLI���g�p����Cognito ID�v�[������ꎞ�I�ȔF�؏����擾�����

1. Cognito���[�U�[�v�[���ŃT�C���C�����s��JWT�g�[�N�����擾����BJWT�g�[�N���̒���ID�g�[�N�������ϐ��ɐݒ肷��

```
ID_TOKEN=(JWT�g�[�N���̒���ID�g�[�N��)
```

2. �K�v�ȏ������ϐ��ɐݒ�

```
REGION=(���[�W����ID)
USER_POOL_ID=(Congnito���[�U�[�v�[����ID)
COGNITO_USER_POOL=cognito-idp.${REGION}.amazonaws.com/${USER_POOL_ID}
IDENTITY_POOL_ID=(Congnito ID�v�[����ID)
```

3. CognitoID�v�[������Identity ID���擾���Ċ��ϐ��ɐݒ�

```
IDENTITY_ID=$(aws cognito-identity get-id \
  --identity-pool-id ${IDENTITY_POOL_ID} \
  --logins "${COGNITO_USER_POOL}=${ID_TOKEN}" \
  --query "IdentityId" \
  --output text) && echo ${IDENTITY_ID}
```

4. Identity ID���g���Ĉꎞ�I�ȔF�؏����擾

```
aws cognito-identity get-credentials-for-identity \
  --identity-id ${IDENTITY_ID} \
  --logins "${COGNITO_USER_POOL}=${ID_TOKEN}"
```

5. �ꎞ�I�ȔF�؏�񂩂�֘A����IAM���[������\������

```
export AWS_ACCESS_KEY_ID=(�ꎞ�I�ȔF�؏��̒��̃A�N�Z�X�L�[ID)
export AWS_SECRET_ACCESS_KEY=(�ꎞ�I�ȔF�؏��̒��̃V�[�N���b�g�A�N�Z�X�L�[)
export AWS_SESSION_TOKEN=(�ꎞ�I�ȔF�؏��̒��̃Z�b�V�����g�[�N��)

aws sts get-caller-identity 
```
6. API Gateway��API��IAM�F�؂�ݒ肵�Ă���ꍇ�A�ꎞ�I�ȔF�؏��̒l����SigV4�ɂ�鏐���L�[���Z�o���āAAuthorization�w�b�_�ɐݒ肵�ă��N�G�X�g�𔭍s����

https://docs.aws.amazon.com/ja_jp/general/latest/gr/signature-v4-examples.html



