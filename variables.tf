variable "org_id" {
  description = "(Required) AWS Organizations ID which you want to allow access to the ECR repository. "
}

variable "tags" {
  description = "(Optional) A map of tags to populate on the created resources. If configured with a provider default_tags configuration block present, tags with matching keys will overwrite those defined at the provider-level."
  type        = map(string)
  default     = {}
}
