# Execution tracer for visualization generation

module Tracer
  @@trace_enabled = false
  @@trace_data = []

  def self.enable!
    @@trace_enabled = true
    @@trace_data = []
  end

  def self.disable!
    @@trace_enabled = false
  end

  def self.enabled?
    @@trace_enabled
  end

  def self.data
    @@trace_data
  end

  def self.clear!
    @@trace_data = []
  end

  def self.export_json
    require 'json'
    JSON.pretty_generate({
      version: "1.0",
      traces: @@trace_data
    })
  end

  def trace(event, data = {})
    return unless Tracer.enabled?

    @@trace_data << {
      event: event.to_s,
      timestamp: Time.now.to_f,
      data: data
    }
  end
end
