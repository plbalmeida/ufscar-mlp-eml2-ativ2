terraform {
  backend "s3" {
    region         = "us-east-1"  
    role_arn       = "arn:aws:iam::413467296690:role/ufscar-mlp-eml2-ativ2-terraform-backend-ecr-role"
    bucket         = "ufscar-mlp-eml2-ativ2-terraform-backend-ecr-bucket"
    key            = "terraform.tfstate"
    dynamodb_table = "ufscar-mlp-eml2-ativ2-terraform-backend-ecr-lock-table"
    encrypt        = true
  }
}