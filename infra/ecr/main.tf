resource "aws_ecr_repository" "ufscar_mlp_eml2_ativ2" {
  name                 = "ufscar-mlp-eml2-ativ2"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}
