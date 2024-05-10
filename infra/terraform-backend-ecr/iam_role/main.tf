resource "aws_iam_role" "role" {
  name = "${var.project_name}-terraform-backend-ecr-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          AWS = "arn:aws:iam::${var.account_id}:root"
        }
      }
    ]
  })
}

resource "aws_iam_policy" "policy" {
  name        = "${var.project_name}-terraform-backend-ecr-access-policy"
  description = "Policy that grants full access to accounts-terraform-backend S3 bucket"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow",
        Action = [
          "s3:ListBucket", 
          "s3:GetObject", 
          "s3:PutObject",
          "s3:DeleteObject"
        ],
        Resource = [
          "arn:aws:s3:::${var.project_name}-terraform-backend-ecr-bucket", 
          "arn:aws:s3:::${var.project_name}-terraform-backend-ecr-bucket/*"
        ]
      },
      {
        Effect: "Allow",
        Action: [
          "dynamodb:GetItem",
          "dynamodb:PutItem",
          "dynamodb:DeleteItem"
        ],
        Resource: [
          "arn:aws:dynamodb:${var.region}:${var.account_id}:table/${var.project_name}-terraform-backend-ecr-lock-table"
        ]
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "this" {
  policy_arn = aws_iam_policy.policy.arn
  role       = aws_iam_role.role.name
}