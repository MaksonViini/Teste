resource "aws_s3_bucket" "this" {
  bucket = "${random_pet.bucket.id}-${var.environment}"

  tags = {
    Service = "Terraform teste"

    ManagedBy = "Terraform"

    Environment = var.environment

    Owner = "Makson"
  }
}