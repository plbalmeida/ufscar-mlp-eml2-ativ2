resource "aws_dynamodb_table" "terraform_locks" {
  name           = "${var.project_name}-terraform-backend-ecr-lock-table"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "LockID"
  attribute {
    name = "LockID"
    type = "S"
  }
}
